from encrypt import Encrypt
from decrypt import Decrypt
import os

def r_loop(dir_name): # recursively loop through a folder, adding each file and its complete path to an array
    files = os.listdir(dir_name)
    for f in files:
        if os.path.isdir(dir_name + "/" + f) == 1:
            new_dir = dir_name + "/" + f 
            r_loop(new_dir)
        else:
            all_files.append(dir_name + "/" + f)

def r_encrypt():
    r_loop("test_files")
    print(all_files)
    Encrypt(
        all_files,
        "3b4e434"
    )
def r_decrypt():
    r_loop("test_files")
    print(all_files)
    Decrypt(
        all_files,
        "3b4e434"
    )

