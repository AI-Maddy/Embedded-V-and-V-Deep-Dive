import os
from datetime import date

FRONTMATTER_TEMPLATE = '''---
title: "{title}"
description: "Auto-generated from filename."
pubDate: "{pub_date}"
---
'''

def add_frontmatter_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if content.lstrip().startswith('---'):
        return  # Already has frontmatter
    title = os.path.splitext(os.path.basename(filepath))[0].replace('_', ' ').replace('-', ' ')
    pub_date = date.today().isoformat()
    frontmatter = FRONTMATTER_TEMPLATE.format(title=title, pub_date=pub_date)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)

def process_dir(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.md'):
                add_frontmatter_to_file(os.path.join(dirpath, filename))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python add_frontmatter.py <markdown_dir>')
        exit(1)
    process_dir(sys.argv[1])
    print('Frontmatter added to all markdown files.')
