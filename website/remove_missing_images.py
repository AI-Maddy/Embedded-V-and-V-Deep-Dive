import os
import re

def remove_missing_images(root):
    image_pattern = re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if not filename.endswith('.md'):
                continue
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Remove image references to _images/ or images/ or any .svg
            new_content = re.sub(r'!\[[^\]]*\]\(([^)]+_images/[^)]+|[^)]+images/[^)]+|[^)]+\.svg)\)', '', content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python remove_missing_images.py <markdown_dir>')
        exit(1)
    remove_missing_images(sys.argv[1])
    print('Removed missing image references.')
