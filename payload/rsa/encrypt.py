from key import Key
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import zlib
import base64

class Encrypt():
    def __init__(self, files, key_hash):
        key = Key()
        raw_key = key.load(key_hash)
        self.rsa_key = RSA.importKey(raw_key)
        self.rsa_key = PKCS1_OAEP.new(self.rsa_key)
        self.files = files
        for f in self.files:
            self.encrypt(f)
    def encrypt(self, file_name):
        raw_data = None
        with open(file_name, "rb") as f:
            raw_data = fd.read()

    

        raw_data = zlib.compress(raw_data) # First, compress the data of the file

        # In determining the chunk size, determine the private key length used in bytes
        # and subtract 42 bytes (when using PKCS1_OAEP). The data will be in encrypted in chunks

        chunk_size = 470
        offset = 0
        encrypted =  "" # String storing the current encrypted file
        end_loop = False
        while not end_loop:
            chunk = blob[offset:offset + chunk_size] # Current chunk
            if len(chunk) % chunk_size != 0: # Add padding, this means that the loop reached the end of the file
                end_loop = True
                chunk += " " * (chunk_size - len(chunk))
            encrypted += rsa_key.encrypt(chunk) # Append the encrypted chunk to the overall encrypted file
            offset += chunk_size # Increase the offset by chunk size
        return base64.b64encode(encrypted) # Base 64 encode the encrypted file


        #Write the encrypted contents to a file
        fd = open("encrypted_img.jpg", "wb")
        fd.write(encrypted_blob)
        fd.close()

Encrypt(
    [
        "test/test1",
        "test/test2",
    ],
    "607dbef"
)
#Our candidate file to be encrypted
