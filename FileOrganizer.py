import os, shutil
from datetime import datetime
import sys
# import tkinter as tk
from tkinter import filedialog
import logging
import mimetypes
import filetype

# def select_dir():
#     selected_directory = filedialog.askdirectory(title="Select a Folder That You Need To Organize")+"/"
#     if selected_directory and os.path.exists(selected_directory):
#         return selected_directory
#     else:
#         print("Invalid directory or directory does not exist.")
#         return None
    
def move(path, folder, file):
    os.makedirs(os.path.join(path, folder), exist_ok=True)
    shutil.move(os.path.join(path, file), os.path.join(path, folder, file))
    os.makedirs(os.path.join(path, 'LOGS'), exist_ok=True)
    log_file_path = os.path.join(path, 'LOGS', 'Move Records.log')
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(message)s")
    logging.info(f"Source: {path + file},\nDestination: {path + folder + file},\nTime: {current_time}\n\n")

def main():
    # path = r"C:/Users/ASUS/Documents/CodeRep/FileOrganizer/"
    # path = select_dir()
    path = sys.argv[1]+"/"
    fileName = os.listdir(path)
    folderName = {
        ".html5": "TEXT/HTML",
        ".docx": "APPLICATION/MSWORD",
        ".xlsx": "application/vnd.ms-excel",
        ".pptx": "application/vnd.ms-powerpoint",
        ".cpp" : "text/c++",
        ".c++" : "text/c++",
        ".java": "text/java",
        ".iso": "application/octet-stream",
        "._": "OTHER FILES/Light Weight Copy"
    }

    for file in fileName:
        if not os.path.isfile(path+file):
            continue
        mime_type, _ = mimetypes.guess_type(file)
        if mime_type:
            mime_type = mime_type.upper()
            # print(mime_type)
            move(path, mime_type, file)
        else:
            _, ext = os.path.splitext(file)
            if ext == "":
                move(path, "BLANK FILES/", file)
            else:
                folder = folderName.get(ext.lower())
                if folder is not None:
                    move(path, folder.upper(), file)  
                else:
                    name = (ext[1:].upper())
                    print(name)
                    move(path, ("OTHER FILES/"+name), file)

if __name__ == "__main__":
    main()