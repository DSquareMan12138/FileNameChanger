import os
import shutil

folder_path = r"D:\BaiduNetdiskDownload\4"   # ← change this

def change_suffix(folder_path, suffix):
    """
    Rename all files in the given folder to .7z suffix.
    Only affects files in this folder (no subfolders).
    """
    suffix = str(suffix)
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isfile(full_path):
            name, ext = os.path.splitext(filename)

            # Skip files already the suffix
            if ext.lower() != suffix:
                new_name = name + suffix
                new_path = os.path.join(folder_path, new_name)

                os.rename(full_path, new_path)
                print(f"Renamed: {filename} → {new_name}")

    print("Done.")

def move_all_files_to_one_folder(src_root, dst_folder, suffix, rename_to_suffix=False):
    """
    Move every file under src_root (including subfolders) into dst_folder.
    Optionally rename file suffix to .7z (rename only, no compression).

    Handles filename collisions by appending _1, _2, ...
    """
    os.makedirs(dst_folder, exist_ok=True)

    suffix = str(suffix)

    def unique_path(folder, filename):
        base, ext = os.path.splitext(filename)
        candidate = os.path.join(folder, filename)
        k = 1
        while os.path.exists(candidate):
            candidate = os.path.join(folder, f"{base}_{k}{ext}")
            k += 1
        return candidate

    moved = 0
    for root, _, files in os.walk(src_root):
        # avoid re-processing files if dst_folder is inside src_root
        if os.path.abspath(root).startswith(os.path.abspath(dst_folder) + os.sep):
            continue

        for filename in files:
            src_path = os.path.join(root, filename)

            # decide destination filename
            base, ext = os.path.splitext(filename)
            if rename_to_suffix and ext.lower() != suffix:
                dst_name = base + suffix
            else:
                dst_name = filename

            dst_path = unique_path(dst_folder, dst_name)

            shutil.move(src_path, dst_path)
            moved += 1
            print(f"Moved: {src_path} -> {dst_path}")

    print(f"Done. Moved {moved} file(s).")