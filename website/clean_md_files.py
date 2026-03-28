import os
from datetime import datetime
import re

# Optional: pip install mdformat or mdutils if you want advanced formatting
try:
    import mdformat
except ImportError:
    mdformat = None

def is_valid_iso_date(date_str):
    try:
        datetime.fromisoformat(date_str)
        return True
    except Exception:
        return False

def clean_frontmatter(lines):
    """
    Ensures frontmatter block is at the top, with required fields and correct ISO date format.
    Returns (cleaned_lines, changed:bool)
    """
    changed = False
    # Remove all lines before the first ---
    start = 0
    while start < len(lines) and not lines[start].strip().startswith('---'):
        start += 1
    if start >= len(lines):
        return lines, changed  # No frontmatter found
    # Find end of first frontmatter block
    fm_end = None
    for i in range(start+1, min(start+40, len(lines))):
        if lines[i].strip().startswith('---'):
            fm_end = i
            break
    if fm_end is None:
        return lines, changed  # Malformed frontmatter
    fm_lines = lines[start+1:fm_end]
    # Remove any additional frontmatter blocks or stray fields after fm_end
    body = []
    in_fm = False
    for i in range(fm_end+1, len(lines)):
        l = lines[i]
        if l.strip().startswith('---'):
            in_fm = not in_fm
            changed = True
            continue
        if in_fm:
            changed = True
            continue
        # Remove lines that look like frontmatter fields outside the block
        if re.match(r'^[a-zA-Z0-9_\-]+\s*:', l):
            changed = True
            continue
        body.append(l)
    fm_dict = {}
    for l in fm_lines:
        if ':' in l:
            k, v = l.split(':', 1)
            fm_dict[k.strip()] = v.strip().strip('"\'')
    # Required fields
    required = ['title', 'description', 'pubDate']
    for r in required:
        if r not in fm_dict or not fm_dict[r]:
            fm_dict[r] = f"FIXME_{r}"  # Placeholder
            changed = True
    # Fix date
    if not is_valid_iso_date(fm_dict['pubDate']):
        # Try to parse common formats
        try:
            dt = datetime.strptime(fm_dict['pubDate'], '%Y-%m-%d')
        except Exception:
            try:
                dt = datetime.strptime(fm_dict['pubDate'], '%b %d %Y')
            except Exception:
                dt = datetime.now()
        fm_dict['pubDate'] = dt.date().isoformat()
        changed = True
    # Rebuild frontmatter
    new_fm = ['---']
    for k in required:
        new_fm.append(f"{k}: {fm_dict[k]}")
    # Add any extra fields
    for k in fm_dict:
        if k not in required:
            new_fm.append(f"{k}: {fm_dict[k]}")
    new_fm.append('---')
    cleaned = new_fm + [''] + body
    return cleaned, changed

def clean_md_file(path):
    print(f"[DEBUG] Processing: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    cleaned, changed = clean_frontmatter(lines)
    lines_changed = 0
    if changed:
        # Count changed lines
        lines_changed = sum(1 for a, b in zip(lines, cleaned) if a != b) + abs(len(lines) - len(cleaned))
        print(f"[DEBUG] Fixed frontmatter in: {path} | Lines changed: {lines_changed}")
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(cleaned) + '\n')
    else:
        print(f"[DEBUG] No changes needed for: {path}")
    # Optionally format markdown body
    if mdformat:
        print(f"[DEBUG] Formatting markdown with mdformat: {path}")
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        formatted = mdformat.text(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(formatted)
    return changed, lines_changed

def scan_and_clean(root):
    print(f"[DEBUG] Scanning directory: {root}")
    total_files = 0
    changed_files = 0
    total_lines_changed = 0
    changed_file_details = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith('.md'):
                path = os.path.join(dirpath, fn)
                print(f"[DEBUG] Found markdown file: {path}")
                total_files += 1
                changed, lines_changed = clean_md_file(path)
                if changed:
                    changed_files += 1
                    total_lines_changed += lines_changed
                    changed_file_details.append((path, lines_changed))
    print(f"[DEBUG] Scan complete for: {root}")
    print(f"[SUMMARY] Markdown files processed: {total_files}")
    print(f"[SUMMARY] Files changed: {changed_files}")
    print(f"[SUMMARY] Total lines changed: {total_lines_changed}")
    if changed_file_details:
        print(f"[SUMMARY] Changed files and lines changed:")
        for path, lines in changed_file_details:
            print(f"    {path}: {lines} lines changed")
    # Write summary to log file
    with open("md_cleanup_summary.log", "w", encoding="utf-8") as logf:
        logf.write(f"Markdown files processed: {total_files}\n")
        logf.write(f"Files changed: {changed_files}\n")
        logf.write(f"Total lines changed: {total_lines_changed}\n")
        if changed_file_details:
            logf.write(f"Changed files and lines changed:\n")
            for path, lines in changed_file_details:
                logf.write(f"    {path}: {lines} lines changed\n")

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"[DEBUG] Starting markdown cleanup in: {root}")
    scan_and_clean(root)
    print("[DEBUG] Markdown cleanup complete.")
