import os
import re
from ruamel.yaml import YAML
from datetime import date

def is_frontmatter_valid(frontmatter):
    yaml = YAML()
    try:
        yaml.load(frontmatter)
        return True
    except Exception:
        return False

def fix_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.lstrip().startswith('---'):
        return  # No frontmatter to fix
    parts = content.split('---', 2)
    if len(parts) < 3:
        return  # Malformed frontmatter
    _, frontmatter, body = parts
    # Remove bad indentation
    lines = [line.rstrip() for line in frontmatter.splitlines()]
    fixed = '\n'.join(lines)
    # Validate YAML
    if not is_frontmatter_valid(fixed):
        # Fallback: minimal valid frontmatter
        # Remove non-ASCII and special characters from title
        raw_title = os.path.splitext(os.path.basename(filepath))[0].replace('_', ' ').replace('-', ' ')
        title = ''.join(c for c in raw_title if c.isalnum() or c in (' ', '.', '_', '-')).strip()
        pub_date = date.today().isoformat()
        fixed = f'title: "{title}"\ndescription: "Auto-fixed frontmatter."\npubDate: "{pub_date}"\n'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'---\n{fixed}\n---\n{body}')

def process_dir(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.md'):
                fix_frontmatter(os.path.join(dirpath, filename))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python fix_frontmatter.py <markdown_dir>')
        exit(1)
    process_dir(sys.argv[1])
    print('Frontmatter fixed for all markdown files.')
