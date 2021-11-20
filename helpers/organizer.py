import os, sys, time
from pathlib import Path 
from .files import *
import shutil
from tqdm import tqdm
# from .progress_bar import progressBar

def organize_junk(dir):
    if(not os.path.isdir(dir)): 
        return "Not a dir"
    i = 1
    size = len(os.listdir(dir))
    for entry in tqdm(os.scandir(dir)):
        time.sleep(1)
        # print("Position " + str(i) + " of " + str(size) + " files.\n\n")
        # print("----------------------------------------------------------------------------- \n \n")
        i+= 1
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        
        if file_format in FILE_FORMATS:
            dir_to_save = dir + "\\" + FILE_FORMATS[file_format]
            if not os.path.isdir(dir_to_save):
                os.mkdir(dir_to_save)
            
            shutil.move(file_path , dir_to_save)

        
    return "Dir organized"