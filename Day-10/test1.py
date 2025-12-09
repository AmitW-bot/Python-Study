#  list all the files in list of folders that user provide as input print maximimum size of it and handle exception if folder is not found

import os
folders = input("Enter folder names separated by space: ").split()
for folder in folders:
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print(f"Folder '{folder}' not found, please provide correct folder name.")
    except PermissionError:
        print(f"Permission denied to access folder '{folder}'.")
        continue
    print("listing given folder:", folder)
    for file in files:
        print(file)
        
