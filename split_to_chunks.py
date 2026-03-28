import os
import re
from pathlib import Path

# Supported heading patterns
MD_HEADING_PATTERN = re.compile(r'^(#{2,6})\s+(.*)')  # ##, ###, etc.
RST_HEADING_CHARS = ['=', '-', '~', '^', '"', '#', '*', '+', '`', ':', '.']


def split_markdown(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunks = []
    current_chunk = []
    current_title = None

    for line in lines:
        match = MD_HEADING_PATTERN.match(line)
        if match:
            if current_chunk and current_title:
                chunks.append((current_title, current_chunk))
                current_chunk = []
            current_title = match.group(2).strip().replace('/', '_')
        if current_title:
            current_chunk.append(line)

    if current_chunk and current_title:
        chunks.append((current_title, current_chunk))

    for idx, (title, chunk) in enumerate(chunks):
        safe_title = title if title else f'chunk_{idx+1}'
        base_path = os.path.join(output_dir, f'{safe_title}.md')
        out_path = base_path
        count = 2
        while os.path.exists(out_path):
            out_path = os.path.join(output_dir, f'{safe_title}_{count}.md')
            count += 1
        with open(out_path, 'w', encoding='utf-8') as f:
            f.writelines(chunk)


def split_rst(file_path, output_dir):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chunks = []
    current_chunk = []
    current_title = None
    for i, line in enumerate(lines):
        # Look for rst heading underline/overline
        if i+1 < len(lines):
            for char in RST_HEADING_CHARS:
                if (set(lines[i+1].strip()) == {char} and
                        len(lines[i+1].strip()) >= len(line.strip()) and
                        line.strip()):
                    if current_chunk and current_title:
                        chunks.append((current_title, current_chunk))
                        current_chunk = []
                    current_title = line.strip().replace('/', '_')
        if current_title:
            current_chunk.append(line)
    if current_chunk and current_title:
        chunks.append((current_title, current_chunk))
    for idx, (title, chunk) in enumerate(chunks):
        safe_title = title if title else f'chunk_{idx+1}'
        base_path = os.path.join(output_dir, f'{safe_title}.rst')
        out_path = base_path
        count = 2
        while os.path.exists(out_path):
            out_path = os.path.join(output_dir, f'{safe_title}_{count}.rst')
            count += 1
        with open(out_path, 'w', encoding='utf-8') as f:
            f.writelines(chunk)


def process_directory(root_dir, output_base):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md') or filename.endswith('.rst'):
                file_path = os.path.join(dirpath, filename)
                rel_dir = os.path.relpath(dirpath, root_dir)
                output_dir = os.path.join(output_base, rel_dir)
                Path(output_dir).mkdir(parents=True, exist_ok=True)
                if filename.endswith('.md'):
                    split_markdown(file_path, output_dir)
                else:
                    split_rst(file_path, output_dir)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print('Usage: python split_to_chunks.py <input_dir> <output_dir>')
        sys.exit(1)
    process_directory(sys.argv[1], sys.argv[2])
    print('Splitting complete.')
