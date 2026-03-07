#!/usr/bin/env python3
"""
check_intra_duplication.py — Detect intra-file (within a single file) repetition.

Checks performed on every RST file:
  1. Duplicate lines       — same non-trivial line appears ≥ N times
  2. Duplicate paragraphs  — same paragraph block appears ≥ N times
  3. Duplicate sections    — same section heading appears ≥ 2 times
  4. Duplicate n-grams     — consecutive line sequences that repeat inside the file
  5. High line-repeat ratio — % of lines that are duplicated (catches bloated files)

Usage:
    # Scan all RST files under the repo root
    python3 check_intra_duplication.py

    # Scan a specific file
    python3 check_intra_duplication.py --file path/to/file.rst

    # Scan a directory with custom thresholds
    python3 check_intra_duplication.py --root ./01_Foundations_and_MIL \
        --min-line-repeats 3 --min-para-repeats 2 --ngram 4

    # Auto-fix: remove exact duplicate paragraphs (keeps first occurrence)
    python3 check_intra_duplication.py --fix

    # Output CSV
    python3 check_intra_duplication.py --csv report.csv

Exit codes:
    0 — clean
    1 — duplicates found (or fixed)
"""

import argparse
import csv
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterator

# ---------------------------------------------------------------------------
# RST section-underline characters (PEP / Sphinx convention)
# ---------------------------------------------------------------------------
RST_UNDERLINE_CHARS = set("=-~^\"'`+#*:<>_")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _clean(line: str) -> str:
    """Strip ANSI codes and surrounding whitespace."""
    return re.sub(r"\x1b\[[0-9;]*m", "", line).strip()


def _is_underline(line: str) -> bool:
    stripped = line.strip()
    return bool(stripped) and len(set(stripped)) == 1 and stripped[0] in RST_UNDERLINE_CHARS


def _is_trivial(line: str) -> bool:
    """Return True for lines too short / structural to be meaningful duplicates."""
    s = line.strip()
    if len(s) < 12:
        return True
    if _is_underline(s):
        return True
    # RST directives, field list markers, plain separators
    if re.match(r"^\.\.[ ]|^\|[ ]|^\+[-=+]+\+$|^[-=~^]+$", s):
        return True
    return False


def _paragraphs(lines: list[str]) -> list[tuple[str, int]]:
    """
    Split lines into paragraphs.
    Returns list of (paragraph_text, start_line_1based).
    """
    result: list[tuple[str, int]] = []
    current: list[str] = []
    start = 0
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped:
            if not current:
                start = i + 1
            current.append(stripped)
        else:
            if current:
                result.append(("\n".join(current), start))
            current = []
    if current:
        result.append(("\n".join(current), start))
    return result


def _section_headings(lines: list[str]) -> list[tuple[str, int]]:
    """
    Return (heading_text, line_number_1based) for each RST section heading.
    A heading is a non-underline line immediately followed by an underline.
    """
    headings: list[tuple[str, int]] = []
    for i in range(len(lines) - 1):
        text = lines[i].strip()
        nxt  = lines[i + 1].strip()
        if text and nxt and _is_underline(nxt) and len(nxt) >= len(text):
            headings.append((text, i + 1))
    return headings


def _ngrams(lines: list[str], n: int) -> Iterator[tuple[tuple[str, ...], int]]:
    """Yield (ngram_tuple, start_line_1based) for every n-gram of non-trivial lines."""
    clean = [(_clean(l), idx + 1) for idx, l in enumerate(lines) if not _is_trivial(_clean(l))]
    for i in range(len(clean) - n + 1):
        gram = tuple(t for t, _ in clean[i:i + n])
        yield gram, clean[i][1]


# ---------------------------------------------------------------------------
# Detectors
# ---------------------------------------------------------------------------

def detect_duplicate_lines(lines: list[str], min_repeats: int = 3) -> list[dict]:
    issues: list[dict] = []
    clean_lines = [_clean(l) for l in lines]
    counts = Counter(l for l in clean_lines if not _is_trivial(l))
    for text, count in counts.items():
        if count >= min_repeats:
            occurrences = [i + 1 for i, l in enumerate(clean_lines) if l == text]
            issues.append({
                "check":      "duplicate_line",
                "count":      count,
                "lines":      occurrences,
                "excerpt":    text[:160],
            })
    return sorted(issues, key=lambda x: -x["count"])


def detect_duplicate_paragraphs(lines: list[str], min_repeats: int = 2) -> list[dict]:
    issues: list[dict] = []
    paras = _paragraphs(lines)
    # Index: text → list of start lines
    index: dict[str, list[int]] = defaultdict(list)
    for text, start in paras:
        if len(text) > 30:
            index[text].append(start)
    for text, starts in index.items():
        if len(starts) >= min_repeats:
            issues.append({
                "check":   "duplicate_paragraph",
                "count":   len(starts),
                "lines":   starts,
                "excerpt": text[:200].replace("\n", " ↵ "),
            })
    return sorted(issues, key=lambda x: -x["count"])


def detect_duplicate_sections(lines: list[str]) -> list[dict]:
    issues: list[dict] = []
    headings = _section_headings(lines)
    index: dict[str, list[int]] = defaultdict(list)
    for text, lineno in headings:
        index[text.lower()].append(lineno)
    for text, linenos in index.items():
        if len(linenos) >= 2:
            issues.append({
                "check":   "duplicate_section",
                "count":   len(linenos),
                "lines":   linenos,
                "excerpt": text[:160],
            })
    return sorted(issues, key=lambda x: -x["count"])


def detect_duplicate_ngrams(lines: list[str], n: int = 4) -> list[dict]:
    issues: list[dict] = []
    gram_map: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for gram, start in _ngrams(lines, n):
        gram_map[gram].append(start)
    for gram, starts in gram_map.items():
        if len(starts) >= 2:
            issues.append({
                "check":   f"duplicate_{n}gram",
                "count":   len(starts),
                "lines":   starts,
                "excerpt": " | ".join(gram)[:200],
            })
    return sorted(issues, key=lambda x: -x["count"])


def detect_high_repeat_ratio(lines: list[str], threshold: float = 0.35) -> list[dict]:
    """Flag files where >threshold fraction of meaningful lines are repeated."""
    meaningful = [_clean(l) for l in lines if not _is_trivial(_clean(l))]
    if len(meaningful) < 20:
        return []
    counts = Counter(meaningful)
    repeated = sum(1 for l, c in counts.items() if c >= 2) if counts else 0
    ratio = repeated / len(counts) if counts else 0.0
    if ratio >= threshold:
        return [{
            "check":   "high_repeat_ratio",
            "count":   repeated,
            "lines":   [],
            "excerpt": f"{ratio:.0%} of unique meaningful lines are duplicated ({repeated}/{len(counts)})",
        }]
    return []


# ---------------------------------------------------------------------------
# Auto-fix
# ---------------------------------------------------------------------------

def fix_duplicate_paragraphs(path: Path) -> bool:
    """
    Remove all but the first occurrence of each duplicate paragraph.
    Returns True if the file was modified.
    """
    text = path.read_text(errors="replace")
    lines = text.splitlines(keepends=True)
    paras = _paragraphs([l.rstrip("\n") for l in lines])

    seen: set[str] = set()
    keep_starts: set[int] = set()    # 1-based start lines to KEEP
    keep_para_texts: set[str] = set()

    # First pass: find which occurrences to keep (first = keep, rest = drop)
    for ptext, start in paras:
        norm = ptext.strip()
        if len(norm) <= 30:
            keep_starts.add(start)  # trivial — always keep
            continue
        if norm not in seen:
            seen.add(norm)
            keep_starts.add(start)
            keep_para_texts.add(norm)

    if not keep_para_texts:
        return False

    # Rebuild: walk paragraph by paragraph, drop duplicate occurrences
    seen2: set[str] = set()
    result_lines: list[str] = []
    para_iter = iter(_paragraphs([l.rstrip("\n") for l in lines]))

    # Build a quick set of duplicate paragraph texts
    counts = Counter(pt for pt, _ in _paragraphs([l.rstrip("\n") for l in lines]) if len(pt) > 30)
    dup_texts = {pt for pt, cnt in counts.items() if cnt >= 2}

    # Reconstruct by going through raw lines and skipping duplicate para blocks
    raw_lines = [l.rstrip("\n") for l in lines]
    # Map line index (0-based) → paragraph text if it starts a dup paragraph
    line_to_para: dict[int, str] = {}
    for ptext, start in _paragraphs(raw_lines):
        if ptext in dup_texts:
            line_to_para[start - 1] = ptext  # 0-based

    i = 0
    while i < len(raw_lines):
        if i in line_to_para:
            ptext = line_to_para[i]
            para_line_count = len(ptext.splitlines())
            if ptext in seen2:
                # skip this paragraph block + following blank lines
                i += para_line_count
                while i < len(raw_lines) and not raw_lines[i].strip():
                    i += 1
                continue
            else:
                seen2.add(ptext)
        result_lines.append(lines[i])
        i += 1

    new_text = "".join(result_lines)
    if new_text != text:
        path.write_text(new_text)
        return True
    return False


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

SEVERITY = {
    "duplicate_section":     "🔴",
    "high_repeat_ratio":     "🔴",
    "duplicate_paragraph":   "🟡",
    "duplicate_line":        "🟠",
}

def _sev(check: str) -> str:
    for k, v in SEVERITY.items():
        if k in check:
            return v
    return "⚪"


def print_file_report(path: Path, all_issues: list[dict], root: Path) -> None:
    try:
        rel = path.relative_to(root)
    except ValueError:
        rel = path
    print(f"\n{'─'*72}")
    print(f"  📄  {rel}  —  {len(all_issues)} issue(s)")
    print(f"{'─'*72}")
    for iss in all_issues:
        sev  = _sev(iss["check"])
        lnos = ", ".join(str(n) for n in iss["lines"][:6])
        lnos = f"  lines: {lnos}" if lnos else ""
        print(f"  {sev}  [{iss['check']}]  ×{iss['count']}{lnos}")
        print(f"      ↳ {iss['excerpt'][:130]}")


def print_summary(total_files: int, affected: int, total_issues: int) -> None:
    print(f"\n{'═'*72}")
    print(f"  Intra-file Duplication Summary")
    print(f"{'═'*72}")
    print(f"  Files scanned  : {total_files}")
    print(f"  Files affected : {affected}")
    print(f"  Total issues   : {total_issues}")
    print(f"{'═'*72}\n")


def write_csv(rows: list[dict], csv_path: str) -> None:
    fields = ["file", "check", "count", "lines", "excerpt"]
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"📄  CSV written: {csv_path}  ({len(rows)} rows)")


# ---------------------------------------------------------------------------
# Per-file analysis
# ---------------------------------------------------------------------------

def analyse_file(
    path: Path,
    min_line_repeats: int,
    min_para_repeats: int,
    ngram_size: int,
    ratio_threshold: float,
) -> list[dict]:
    try:
        raw = path.read_text(errors="replace")
    except Exception as exc:
        print(f"  [WARN] Cannot read {path}: {exc}", file=sys.stderr)
        return []

    lines = raw.splitlines()
    issues: list[dict] = []
    issues += detect_duplicate_lines(lines, min_line_repeats)
    issues += detect_duplicate_paragraphs(lines, min_para_repeats)
    issues += detect_duplicate_sections(lines)
    if ngram_size >= 2:
        issues += detect_duplicate_ngrams(lines, ngram_size)
    issues += detect_high_repeat_ratio(lines, ratio_threshold)
    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def collect_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.rst"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Detect intra-file duplication in RST files.")
    ap.add_argument("--root",              default=".",      help="Directory to scan (default: .)")
    ap.add_argument("--file",              metavar="RST",    help="Check a single file instead")
    ap.add_argument("--min-line-repeats",  type=int, default=3,    help="Min duplicate line count (default: 3)")
    ap.add_argument("--min-para-repeats",  type=int, default=2,    help="Min duplicate paragraph count (default: 2)")
    ap.add_argument("--ngram",             type=int, default=4,    help="N-gram size for sequence check (0=off, default: 4)")
    ap.add_argument("--ratio-threshold",   type=float, default=0.35, help="Repeated-line ratio to flag (default: 0.35)")
    ap.add_argument("--fix",               action="store_true", help="Auto-remove duplicate paragraphs (keeps first)")
    ap.add_argument("--csv",               metavar="FILE",   help="Write results to CSV")
    ap.add_argument("--quiet",             action="store_true", help="Suppress per-file detail, show summary only")
    args = ap.parse_args()

    root = Path(args.root).resolve()

    if args.file:
        files = [Path(args.file).resolve()]
    else:
        files = collect_files(root)
        print(f"🔍  Scanning {len(files)} RST files under {root} …")

    total_issues  = 0
    affected      = 0
    csv_rows: list[dict] = []
    fixed_count   = 0

    for i, path in enumerate(files, 1):
        if not args.file and not args.quiet:
            print(f"\r  [{i:4}/{len(files)}] {path.name:<45}", end="", flush=True)

        issues = analyse_file(
            path,
            args.min_line_repeats,
            args.min_para_repeats,
            args.ngram,
            args.ratio_threshold,
        )

        if issues:
            affected += 1
            total_issues += len(issues)

            if not args.quiet:
                if not args.file:
                    print()   # end progress line
                print_file_report(path, issues, root)

            if args.csv:
                for iss in issues:
                    csv_rows.append({
                        "file":    str(path),
                        "check":   iss["check"],
                        "count":   iss["count"],
                        "lines":   ";".join(str(n) for n in iss["lines"][:8]),
                        "excerpt": iss["excerpt"][:200],
                    })

            if args.fix:
                if fix_duplicate_paragraphs(path):
                    fixed_count += 1
                    print(f"  ✅  Fixed duplicate paragraphs in: {path.name}")

    if not args.file:
        if not args.quiet:
            print()   # newline after final progress char
        print_summary(len(files), affected, total_issues)

    if args.csv:
        write_csv(csv_rows, args.csv)

    if args.fix and fixed_count:
        print(f"🔧  Auto-fixed {fixed_count} file(s). Re-run without --fix to verify.")

    return 1 if total_issues else 0


if __name__ == "__main__":
    sys.exit(main())
