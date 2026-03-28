import os
import re
from datetime import date

def clean_frontmatter(filepath):
    # Remove all frontmatter blocks and insert a new valid one
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Remove all lines between --- blocks at the top
    new_lines = []
    in_fm = False
    fm_found = False
    for i, line in enumerate(lines):
        if line.strip() == '---' and not fm_found:
            in_fm = not in_fm
            fm_found = True
            continue
        if in_fm:
            if line.strip() == '---':
                in_fm = False
            continue
        new_lines.append(line)
    # Generate new frontmatter
    filename = os.path.basename(filepath)
    title = os.path.splitext(filename)[0]
    # Remove emojis and extra spaces from title
    title = re.sub(r'[^\w\s-]', '', title).replace('_', ' ').replace('-', ' ').strip()
    description = "Auto-generated from filename."
    pub_date = date.today().isoformat()
    frontmatter = f"---\ntitle: \"{title}\"\ndescription: \"{description}\"\npubDate: {pub_date}\n---\n\n"
    # Write new file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.writelines(new_lines)

def scan_and_clean(root):
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith('.md'):
                path = os.path.join(dirpath, fn)
                try:
                    clean_frontmatter(path)
                    print(f"[CLEANED] {path}")
                except Exception as e:
                    print(f"[ERROR] {path}: {e}")

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    scan_and_clean(root)
    print("[DONE] Markdown frontmatter cleaning complete.")
