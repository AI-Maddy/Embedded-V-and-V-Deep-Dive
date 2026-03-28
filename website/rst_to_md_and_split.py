import os
import shutil
import re
from pathlib import Path
import pypandoc

def safe_filename(name):
    # Replace spaces and special chars, keep .md
    name = re.sub(r'[^\w\-\.]+', '_', name)
    return name

def convert_rst_to_md(rst_path, out_dir):
    base = os.path.basename(rst_path)
    folder = os.path.basename(os.path.dirname(rst_path))
    name, _ = os.path.splitext(base)
    md_name = safe_filename(name) + '.md'
    out_path = os.path.join(out_dir, md_name)
    conflict = False
    if os.path.exists(out_path):
        conflict = True
        md_name = safe_filename(folder + '_' + name) + '.md'
        out_path = os.path.join(out_dir, md_name)
    output = pypandoc.convert_file(rst_path, 'md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(output)
    return out_path, conflict

def split_md_file(md_path, split_dir, chunk_size=100):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
    base = os.path.splitext(os.path.basename(md_path))[0]
    split_files = []
    for idx, chunk in enumerate(chunks):
        chunk_name = f'{base}_part{idx+1}.md' if len(chunks) > 1 else f'{base}.md'
        chunk_path = os.path.join(split_dir, chunk_name)
        # Avoid name conflict
        count = 1
        orig_chunk_path = chunk_path
        while os.path.exists(chunk_path):
            chunk_path = orig_chunk_path.replace('.md', f'_{count}.md')
            count += 1
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.writelines(chunk)
        split_files.append(chunk_path)
    return split_files

def main(rst_folders, md_output_dir, split_output_dir, chunk_size=100):
    os.makedirs(md_output_dir, exist_ok=True)
    os.makedirs(split_output_dir, exist_ok=True)
    all_md_paths = []
    rst_count = 0
    conflict_count = 0
    split_folder_count = 0
    split_md_file_count = 0
    conflict_files = []
    # 1. Convert rst to md
    print("[STATS] Starting RST to MD conversion...")
    for folder in rst_folders:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith('.rst'):
                    rst_count += 1
                    rst_path = os.path.join(root, file)
                    md_path, conflict = convert_rst_to_md(rst_path, md_output_dir)
                    all_md_paths.append(md_path)
                    if conflict:
                        conflict_count += 1
                        conflict_files.append(md_path)
    print(f"[STATS] Total .rst files processed: {rst_count}")
    print(f"[STATS] Filename conflicts resolved: {conflict_count}")
    if conflict_files:
        print("[STATS] Conflicted files:")
        for f in conflict_files:
            print(f"    {f}")
    # 2. For each md file, create a folder and move the md file
    print("[STATS] Creating folders and splitting MD files...")
    for md_path in all_md_paths:
        base = os.path.splitext(os.path.basename(md_path))[0]
        folder_path = os.path.join(split_output_dir, base)
        if not os.path.exists(folder_path):
            split_folder_count += 1
        os.makedirs(folder_path, exist_ok=True)
        dest_md_path = os.path.join(folder_path, os.path.basename(md_path))
        shutil.copy(md_path, dest_md_path)
        # 3. Split md file into chunks in the same folder
        split_files = split_md_file(dest_md_path, folder_path, chunk_size=chunk_size)
        split_md_file_count += len(split_files)
    print(f"[STATS] New folders created: {split_folder_count}")
    print(f"[STATS] Total split MD files created: {split_md_file_count}")
    print("[STATS] Conversion and splitting complete.")

if __name__ == "__main__":
    # Example usage, update these paths as needed
    rst_folders = [
        '/home/madhavan/projects/Embedded-V-and-V-Deep-Dive/01_Foundations_and_MIL',
        '/home/madhavan/projects/Embedded-V-and-V-Deep-Dive/02_SIL_and_Software_Validation',
        '/home/madhavan/projects/Embedded-V-and-V-Deep-Dive/03_HIL_and_RealTime',
        '/home/madhavan/projects/Embedded-V-and-V-Deep-Dive/domains',
        '/home/madhavan/projects/Embedded-V-and-V-Deep-Dive/tools',
        '/home/madhavan/projects/Embedded-V-and-V-Deep-Dive/examples',
    ]
    md_output_dir = './converted_md_files'
    split_output_dir = './split_md_files'
    main(rst_folders, md_output_dir, split_output_dir, chunk_size=100)
    print('RST to MD conversion and splitting complete.')
