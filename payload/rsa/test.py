from key import Key
from encrypt import Encrypt
from decrypt import Decrypt
import os

def new_key():
    key = Key()
    key.new_key(4096)


def encrypt():
    Encrypt(
        [
            "test_files/test1",
            "test_files/test2"
        ],
        "3b4e434"
    )

all_files = []
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

def decrypt():
    Decrypt(
    [
        "test_files/test1"
    ],
    "3b4e434"
)
decrypt()
# r_encrypt()

