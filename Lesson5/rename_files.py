import os

def rename_files():
    # 1 get file names from a folder
    file_list = os.listdir(r'C:\Users\mtcal\Pictures')
    print(file_list)
    # 2 for each file, rename filename
    for file_name in file_list:
        os.rename(file_name,)

rename_files()
