import os

def CalcFileSize(filename):
    return os.stat(filename).st_size

def show_files(path, all_files):
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(cur_path)
    return all_files

contents = show_files("Q07", [])

for path in contents:
    if os.stat(path).st_size == 47:
        print(path)