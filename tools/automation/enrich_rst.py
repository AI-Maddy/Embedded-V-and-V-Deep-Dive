#!/usr/bin/env python3
"""
enrich_rst.py — Enrich RST files via the GitHub Models API (gpt-4o).

Paid GitHub Copilot subscribers get higher rate limits on GitHub Models.

Requires:
    GITHUB_TOKEN — GitHub PAT (any classic PAT, no scopes needed)

Usage:
    python3 enrich_rst.py <path_to_rst>

Exit codes:
    0  — file enriched (content changed + written)
    2  — file skipped (no change or nothing to do)
    1  — error
"""

import sys
import os
import json
import hashlib
import time
import urllib.request
import urllib.error
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

# GitHub Models API — works with any PAT; paid Copilot subscribers get higher quotas.
# Rate limits (approximate, may vary by account tier):
#   Free tier   : gpt-4o  50/day,  gpt-4o-mini 150/day,  10 req/min
#   Paid Copilot: gpt-4o 300+/day, gpt-4o-mini  500+/day, higher per-min
COPILOT_API_URL = os.environ.get(
    "COPILOT_API_URL", "https://models.inference.ai.azure.com/chat/completions"
)

# Fallback chain: tried left-to-right when the current model hits its daily quota.
# Override the whole chain:  COPILOT_MODELS="gpt-4o,gpt-4o-mini,Mistral-large-2407"
# Override starting model:   COPILOT_MODEL=gpt-4o-mini
#
# Working GitHub Models chat-completion models (verified 2026-03):
#   gpt-4o                        OpenAI GPT-4o          (best quality)
#   gpt-4o-mini                   OpenAI GPT-4o mini
#   Meta-Llama-3.1-405B-Instruct  Meta Llama 3.1 405B
#   Meta-Llama-3.1-8B-Instruct    Meta Llama 3.1 8B     (fallback of last resort)
#
# NOTE: Mistral-large-2407, Meta-Llama-3-70B-Instruct, Meta-Llama-3.1-70B-Instruct,
#       AI21-Jamba-Instruct, Mistral-Nemo, Meta-Llama-3-8B-Instruct all return
#       HTTP 400 unknown_model from the inference endpoint (removed from chain).
_DEFAULT_CHAIN = (
    "gpt-4o,"
    "gpt-4o-mini,"
    "Meta-Llama-3.1-405B-Instruct,"
    "Meta-Llama-3.1-8B-Instruct"
)
MODEL_CHAIN   = [m.strip() for m in
                 os.environ.get("COPILOT_MODELS", _DEFAULT_CHAIN).split(",")
                 if m.strip()]

# Allow a single-model override (keeps backward compat) — places it at front
_override = os.environ.get("COPILOT_MODEL", "").strip()
if _override and _override not in MODEL_CHAIN:
    MODEL_CHAIN.insert(0, _override)
elif _override:
    # Move override to front
    MODEL_CHAIN = [_override] + [m for m in MODEL_CHAIN if m != _override]

# Active-model state file — lets the next process invocation start on the
# already-downgraded model without re-hitting the exhausted one.
_ACTIVE_MODEL_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), ".active_model"
)


def _load_active_model() -> str:
    """Return the persisted active model, or the first in the chain."""
    try:
        saved = Path(_ACTIVE_MODEL_FILE).read_text().strip()
        if saved in MODEL_CHAIN:
            return saved
    except Exception:
        pass
    return MODEL_CHAIN[0]


def _save_active_model(model: str) -> None:
    try:
        Path(_ACTIVE_MODEL_FILE).write_text(model)
    except Exception:
        pass


MAX_TOKENS       = int(os.environ.get("COPILOT_MAX_TOKENS", "4096"))
TEMPERATURE      = float(os.environ.get("COPILOT_TEMPERATURE", "0.3"))
MAX_RETRIES      = int(os.environ.get("COPILOT_MAX_RETRIES", "5"))
DAILY_LIMIT_SECS = 3600  # retry-after > 1 hr ⇒ daily quota hit — try next model

# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are an expert Technical Writer specialising in embedded-systems \
Verification & Validation (V&V) documentation (DO-178C, DO-254, ISO 26262, \
IEC 62304, ARP4754A/4761, ASPICE).

Your task: Rewrite the given RST file so it becomes:
- Rich, colourful, and memorable with emoji icons on every heading
- Includes a domain-specific mnemonic acronym (create one that fits the content)
- Uses a 🟢🟡🔴 severity / priority colour legend
- Contains GIVEN / WHEN / THEN scenario templates (nominal 🟢, boundary 🟡, fault 🔴)
- Has a pre-review checklist with ☐ checkboxes
- Keeps all existing technical content but expands it substantially
- Uses RST admonitions (.. note::, .. warning::, .. important::, .. admonition::)
- Adds relevant domain standards references (wherever applicable)
- Uses RST list-table:: for tabular content

Output ONLY valid RST source — no markdown code fences, no explanations, \
no surrounding text. The output must start directly with the RST title line.
"""


def build_user_prompt(content: str, path: Path) -> str:
    parts = str(path).lower()
    domain = (
        "aerospace" if "aerospace" in parts
        else "automotive" if "automotive" in parts
        else "medical" if "medical" in parts
        else "embedded systems"
    )
    phase = (
        "MIL (Model-in-the-Loop)" if ("mil" in parts or "foundations" in parts)
        else "SIL (Software-in-the-Loop)" if "sil" in parts
        else "HIL (Hardware-in-the-Loop)" if "hil" in parts
        else "V&V"
    )
    return (
        f"File path: {path}\n"
        f"Domain: {domain}\n"
        f"V&V Phase: {phase}\n\n"
        f"--- CURRENT RST CONTENT ---\n{content}\n--- END ---\n\n"
        "Rewrite this RST file following all the rules in the system prompt."
    )

# ---------------------------------------------------------------------------
# Token / API
# ---------------------------------------------------------------------------


def get_github_token() -> str:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        print(
            "\n[ERROR] GITHUB_TOKEN is not set.\n"
            "  export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx\n",
            file=sys.stderr,
        )
        sys.exit(1)
    return token


def _parse_retry_after(err_body: str) -> int:
    """Extract 'Please wait N seconds' from a 429 error body. Returns 0 if not found."""
    try:
        data = json.loads(err_body)
        msg = data.get("error", {}).get("message", "")
        # e.g. "Please wait 85753 seconds before retrying."
        import re
        m = re.search(r"Please wait (\d+) seconds", msg)
        if m:
            return int(m.group(1))
    except Exception:
        pass
    return 0


def _call_model(model: str, content: str, path: Path) -> str:
    """Call a specific model. Returns response text.
    Raises RuntimeError("daily_limit") when the model's daily quota is exhausted.
    Raises SystemExit on unrecoverable errors.
    """
    token = get_github_token()

    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": build_user_prompt(content, path)},
        ],
        "temperature": TEMPERATURE,
        "max_tokens":  MAX_TOKENS,
    }).encode("utf-8")

    headers = {
        "Content-Type":         "application/json",
        "Authorization":        f"Bearer {token}",
        "Accept":               "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    for attempt in range(1, MAX_RETRIES + 2):
        req = urllib.request.Request(
            COPILOT_API_URL, data=payload, headers=headers, method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = json.loads(resp.read().decode("utf-8"))
            break  # success

        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            if e.code == 429:
                wait = _parse_retry_after(err_body)
                if wait > DAILY_LIMIT_SECS:
                    # Signal caller to try next model
                    raise RuntimeError(f"daily_limit:{model}:{wait}")
                if attempt > MAX_RETRIES:
                    print(f"  [429] Still rate-limited after {MAX_RETRIES} retries on {model}.",
                          file=sys.stderr)
                    raise RuntimeError(f"daily_limit:{model}:{wait}")
                wait = max(wait, 7)
                print(f"  [{model}] [429] Rate limited — waiting {wait}s "
                      f"(retry {attempt}/{MAX_RETRIES})...", flush=True)
                time.sleep(wait)
                continue
            if e.code == 400:
                # unknown_model or bad request — skip to next model in chain
                try:
                    err_code = json.loads(err_body).get("error", {}).get("code", "")
                except Exception:
                    err_code = ""
                if err_code == "unknown_model":
                    print(f"  [{model}] HTTP 400 unknown_model — skipping to next model.",
                          file=sys.stderr)
                    raise RuntimeError(f"daily_limit:{model}:0")
            print(f"[ERROR] API HTTP {e.code}: {err_body}", file=sys.stderr)
            sys.exit(1)

        except urllib.error.URLError as e:
            print(f"[ERROR] Network error: {e.reason}", file=sys.stderr)
            sys.exit(1)

    try:
        return body["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError):
        print(f"[ERROR] Unexpected API response: {json.dumps(body)[:400]}", file=sys.stderr)
        sys.exit(1)


def call_copilot(content: str, path: Path) -> str:
    """Try each model in MODEL_CHAIN in order; auto-fallback on daily quota exhaustion."""
    active = _load_active_model()
    # Start from the active (possibly already-downgraded) model
    try:
        start_idx = MODEL_CHAIN.index(active)
    except ValueError:
        start_idx = 0

    for idx in range(start_idx, len(MODEL_CHAIN)):
        model = MODEL_CHAIN[idx]
        print(f"  → GitHub Models API ({model}) — {path.name} ...", flush=True)
        try:
            result = _call_model(model, content, path)
            # Persist the model that actually worked
            _save_active_model(model)
            return result
        except RuntimeError as exc:
            msg = str(exc)
            if msg.startswith("daily_limit:"):
                _, failed_model, wait_secs = msg.split(":", 2)
                hours = int(wait_secs) // 3600
                print(
                    f"  ⚠️  Daily quota exhausted for '{failed_model}' "
                    f"(resets in ~{hours}h).",
                    flush=True,
                )
                next_models = MODEL_CHAIN[idx + 1:]
                if next_models:
                    print(f"  ↩️  Switching to next model: {next_models[0]}", flush=True)
                    continue
                else:
                    print(
                        "\n[RATE LIMIT] All models in the fallback chain have hit their "
                        "daily quota.\n"
                        f"  Chain tried: {' → '.join(MODEL_CHAIN[start_idx:])}\n"
                        "  Checkpoint saved — re-run tomorrow (quotas reset every 24h).\n"
                        "  Custom chain: COPILOT_MODELS=\"modelA,modelB\" bash batch_enrich.sh\n",
                        file=sys.stderr,
                    )
                    sys.exit(1)
            raise  # unexpected RuntimeError — re-raise

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_response(text: str) -> str:
    """Strip accidental markdown code fences the model might add."""
    lines = text.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip() + "\n"

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    if len(sys.argv) < 2:
        print("Usage: enrich_rst.py <path_to_rst>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1]).resolve()

    if not path.exists():
        print(f"[ERROR] File not found: {path}", file=sys.stderr)
        sys.exit(1)

    if path.suffix.lower() != ".rst":
        print(f"[SKIP] Not an RST file: {path}")
        sys.exit(2)

    original = path.read_text(encoding="utf-8")
    original_sha = sha(original)

    enriched = clean_response(call_copilot(original, path))
    enriched_sha = sha(enriched)

    if enriched_sha == original_sha:
        print(f"[SKIP] Copilot returned identical content: {path.name}")
        sys.exit(2)

    # Atomic write via temp file
    tmp = path.with_suffix(".rst.tmp")
    tmp.write_text(enriched, encoding="utf-8")
    tmp.replace(path)

    lines_before = original.count("\n")
    lines_after  = enriched.count("\n")
    delta        = lines_after - lines_before
    sign         = "+" if delta >= 0 else ""
    print(f"[OK]  ENRICHED via Copilot: {path.name}  ({sign}{delta} lines)")
    sys.exit(0)


if __name__ == "__main__":
    main()
