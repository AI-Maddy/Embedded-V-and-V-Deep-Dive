import os
import re
import shutil

def safe_alphanumeric_filename(filename):
    name, ext = os.path.splitext(filename)
    # Replace non-alphanumeric characters with underscores
    safe_name = re.sub(r'[^A-Za-z0-9]', '_', name)
    # Remove consecutive underscores
    safe_name = re.sub(r'_+', '_', safe_name)
    # Remove leading/trailing underscores
    safe_name = safe_name.strip('_')
    return f"{safe_name}{ext}"

def rename_md_files(root):
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith('.md'):
                old_path = os.path.join(dirpath, fn)
                safe_fn = safe_alphanumeric_filename(fn)
                if fn != safe_fn:
                    new_path = os.path.join(dirpath, safe_fn)
                    # Avoid overwriting existing files
                    if os.path.exists(new_path):
                        base, ext = os.path.splitext(safe_fn)
                        i = 1
                        while os.path.exists(os.path.join(dirpath, f"{base}_{i}{ext}")):
                            i += 1
                        new_path = os.path.join(dirpath, f"{base}_{i}{ext}")
                    print(f"[RENAME] {old_path} -> {new_path}")
                    shutil.move(old_path, new_path)

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    rename_md_files(root)
    print("[DONE] All markdown filenames are now alphanumeric.")
