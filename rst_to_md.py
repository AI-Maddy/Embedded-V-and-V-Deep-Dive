import os
from pathlib import Path
import pypandoc

def convert_rst_to_md(input_dir, output_dir):
    for dirpath, _, filenames in os.walk(input_dir):
        for filename in filenames:
            if filename.endswith('.rst'):
                rst_path = os.path.join(dirpath, filename)
                rel_dir = os.path.relpath(dirpath, input_dir)
                md_dir = os.path.join(output_dir, rel_dir)
                Path(md_dir).mkdir(parents=True, exist_ok=True)
                md_filename = os.path.splitext(filename)[0] + '.md'
                md_path = os.path.join(md_dir, md_filename)
                try:
                    output = pypandoc.convert_file(rst_path, 'md')
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(output)
                    print(f"Converted: {rst_path} -> {md_path}")
                except Exception as e:
                    print(f"Failed to convert {rst_path}: {e}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print('Usage: python rst_to_md.py <input_dir> <output_dir>')
        sys.exit(1)
    convert_rst_to_md(sys.argv[1], sys.argv[2])
    print('RST to MD conversion complete.')
