import os

def list_files_in_directory_recursively(dir_path):
    files = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

dir_path = 'C:/Users/timur/Documents/blog/src/assets/pictures/beppu'
files = list_files_in_directory_recursively(dir_path)
for file in files:
    print(file)
