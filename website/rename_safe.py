import os
import re
import unicodedata

def safe_filename(name):
    # Remove emoji and non-ASCII, replace spaces and special chars with _
    name = unicodedata.normalize('NFKD', name)
    name = name.encode('ascii', 'ignore').decode('ascii')
    name = re.sub(r'[\s\(\)\[\]{}#?":|<>*\\/]', '_', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    return name

def rename_all(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        # Rename files
        for filename in filenames:
            if not filename.endswith('.md'):
                continue
            safe_name = safe_filename(filename)
            if filename != safe_name:
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, safe_name))
        # Rename directories
        for dirname in dirnames:
            safe_dir = safe_filename(dirname)
            if dirname != safe_dir:
                os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, safe_dir))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python rename_safe.py <root_dir>')
        exit(1)
    rename_all(sys.argv[1])
    print('Renaming complete.')
