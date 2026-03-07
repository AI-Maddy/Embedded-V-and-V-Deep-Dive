#!/usr/bin/env python3
"""
find_repetitive.py — Detect RST files with repetitive / duplicated content.

Checks two kinds of repetition:
  1. Duplicate LINES     — exact line appears more than N times in the file
  2. Duplicate PARAGRAPHS — same paragraph block appears more than once
  3. Duplicate FILES     — two or more files share identical content (sha256)

Usage:
    # Scan all RST files under the current directory
    python3 find_repetitive.py

    # Scan a specific directory
    python3 find_repetitive.py --root /path/to/project

    # Change thresholds
    python3 find_repetitive.py --min-line-repeats 4 --min-para-repeats 2

    # Show only duplicate-file pairs (skip intra-file checks)
    python3 find_repetitive.py --only-dupes

    # Output as CSV
    python3 find_repetitive.py --csv report.csv

Exit codes:
    0  — no repetition found
    1  — repetition found (details printed / written to CSV)
"""

import argparse
import csv
import hashlib
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _clean(line: str) -> str:
    return ANSI.sub("", line).strip()


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def _paragraphs(text: str) -> list[str]:
    """Split RST text into non-empty paragraphs (double-newline boundaries)."""
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


# ---------------------------------------------------------------------------
# Detectors
# ---------------------------------------------------------------------------

def check_duplicate_lines(path: Path, min_repeats: int = 3) -> list[dict]:
    """Return duplicate lines that appear >= min_repeats times."""
    issues = []
    try:
        lines = [_clean(l) for l in path.read_text(errors="replace").splitlines()]
    except Exception:
        return issues

    counts = Counter(l for l in lines if len(l) > 10)   # ignore short/empty lines
    for line, count in counts.items():
        if count >= min_repeats:
            occurrences = [i + 1 for i, l in enumerate(lines) if l == line]
            issues.append({
                "type":     "duplicate_line",
                "file":     str(path),
                "count":    count,
                "lines":    occurrences,
                "excerpt":  line[:120],
            })
    return issues


def check_duplicate_paragraphs(path: Path, min_repeats: int = 2) -> list[dict]:
    """Return paragraph blocks that appear >= min_repeats times."""
    issues = []
    try:
        text = path.read_text(errors="replace")
    except Exception:
        return issues

    paras = _paragraphs(text)
    counts = Counter(p for p in paras if len(p) > 30)
    for para, count in counts.items():
        if count >= min_repeats:
            issues.append({
                "type":    "duplicate_paragraph",
                "file":    str(path),
                "count":   count,
                "excerpt": para[:200].replace("\n", " ↵ "),
            })
    return issues


def find_duplicate_files(paths: list[Path]) -> list[dict]:
    """Return groups of files that share identical content."""
    hash_map: dict[str, list[Path]] = defaultdict(list)
    for p in paths:
        try:
            hash_map[_sha256(p)].append(p)
        except Exception:
            pass

    issues = []
    for digest, group in hash_map.items():
        if len(group) > 1:
            issues.append({
                "type":    "duplicate_file",
                "count":   len(group),
                "files":   [str(f) for f in group],
                "sha256":  digest[:12],
                "excerpt": "",
            })
    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def collect_rst_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.rst"))


def print_report(
    line_issues: list[dict],
    para_issues: list[dict],
    file_issues: list[dict],
    root: Path,
) -> None:
    total = len(line_issues) + len(para_issues) + len(file_issues)

    def rel(p: str) -> str:
        try:
            return str(Path(p).relative_to(root))
        except ValueError:
            return p

    if not total:
        print("✅  No repetitive content detected.")
        return

    print(f"\n{'═'*70}")
    print(f"  Repetitive Content Report")
    print(f"{'═'*70}")

    if file_issues:
        print(f"\n🔴  DUPLICATE FILES ({len(file_issues)} groups)\n")
        for iss in file_issues:
            print(f"  sha256:{iss['sha256']}…  ({iss['count']} identical files)")
            for f in iss["files"]:
                print(f"    • {rel(f)}")

    if para_issues:
        print(f"\n🟡  DUPLICATE PARAGRAPHS ({len(para_issues)} occurrences)\n")
        for iss in sorted(para_issues, key=lambda x: -x["count"]):
            print(f"  [{iss['count']}×]  {rel(iss['file'])}")
            print(f"        ↳ {iss['excerpt'][:120]}")

    if line_issues:
        print(f"\n🟠  DUPLICATE LINES ({len(line_issues)} occurrences)\n")
        for iss in sorted(line_issues, key=lambda x: -x["count"]):
            lnums = ", ".join(str(n) for n in iss["lines"][:8])
            print(f"  [{iss['count']}×]  {rel(iss['file'])}  (lines: {lnums})")
            print(f"        ↳ {iss['excerpt'][:120]}")

    print(f"\n{'─'*70}")
    print(f"  Total issues: {total}")
    print(f"{'─'*70}\n")


def write_csv(
    line_issues: list[dict],
    para_issues: list[dict],
    file_issues: list[dict],
    csv_path: str,
) -> None:
    rows = []
    for iss in line_issues:
        rows.append({
            "type":    iss["type"],
            "file":    iss["file"],
            "count":   iss["count"],
            "excerpt": iss["excerpt"],
            "extra":   f"lines:{','.join(str(n) for n in iss['lines'][:8])}",
        })
    for iss in para_issues:
        rows.append({
            "type":    iss["type"],
            "file":    iss["file"],
            "count":   iss["count"],
            "excerpt": iss["excerpt"],
            "extra":   "",
        })
    for iss in file_issues:
        for f in iss["files"]:
            rows.append({
                "type":    iss["type"],
                "file":    f,
                "count":   iss["count"],
                "excerpt": f"sha256:{iss['sha256']}",
                "extra":   "",
            })
    with open(csv_path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["type", "file", "count", "excerpt", "extra"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"📄  CSV report written to: {csv_path}  ({len(rows)} rows)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Find repetitive content in RST files.")
    parser.add_argument("--root",             default=".",      help="Root directory to scan (default: .)")
    parser.add_argument("--min-line-repeats", type=int, default=3, help="Min times a line must repeat (default: 3)")
    parser.add_argument("--min-para-repeats", type=int, default=2, help="Min times a paragraph must repeat (default: 2)")
    parser.add_argument("--only-dupes",       action="store_true", help="Only report duplicate files")
    parser.add_argument("--csv",              metavar="FILE",   help="Write results to CSV")
    parser.add_argument("--quiet",            action="store_true", help="Suppress per-file progress")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    files = collect_rst_files(root)
    print(f"🔍  Scanning {len(files)} RST files under {root} …")

    line_issues: list[dict] = []
    para_issues: list[dict] = []

    if not args.only_dupes:
        for i, path in enumerate(files, 1):
            if not args.quiet:
                print(f"\r  [{i:4}/{len(files)}] {path.name:<40}", end="", flush=True)
            line_issues.extend(check_duplicate_lines(path, args.min_line_repeats))
            para_issues.extend(check_duplicate_paragraphs(path, args.min_para_repeats))
        if not args.quiet:
            print()  # newline after progress

    file_issues = find_duplicate_files(files)

    print_report(line_issues, para_issues, file_issues, root)

    if args.csv:
        write_csv(line_issues, para_issues, file_issues, args.csv)

    return 1 if (line_issues or para_issues or file_issues) else 0


if __name__ == "__main__":
    sys.exit(main())
