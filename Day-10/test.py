import os

def list_files_in_folder(folder_path):
    try:
        files=os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "folder not found"
    except PermissionError:
        return None, "persmission denied"
    
   
def main():
        folder_paths= input("Enter folder paths seperated by space:").split()

        for folder_path in folder_paths:
            files, error_message=list_files_in_folder(folder_path)
            if files:
                print(f"files in {folder_path}")
                for file in files:
                    print(file)
            
            else:
                print(f"error in folder {folder_path}: {error_message}")

if __name__=="__main__":
    main()

