from SuffixChanger import *

if __name__ == "__main__":
    #
    # folder = r"D:\BaiduNetdiskDownload\4"
    # change_suffix_to_7z(folder)

    move_all_files_to_one_folder(
        src_root=r"D:\BaiduNetdiskDownload\4\decompress",
        dst_folder=r"D:\BaiduNetdiskDownload\4\decompress down",
        rename_to_suffix=True
    )