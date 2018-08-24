from key import Key
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib

class Decrypt:
    def __init__(self, files, key_hash):
        key = Key()
        raw_key = key.load_private(key_hash)
        self.rsa_key = RSA.importKey(raw_key)
        self.rsa_key = PKCS1_OAEP.new(self.rsa_key)
        self.files = files
        for f in self.files:
            try:
                self.decrypt(f)
            except Exception as e:
                print("could not decrypt file '" + str(f) + "'")
                print(e)
    def decrypt(self, file_name):
        raw_data = None
        with open(file_name, "rb") as rfile:
            raw_data = rfile.read()
        raw_data = base64.b64decode(raw_data) # Base 64 decode the data
        # In determining the chunk size, determine the private key length used in bytes.
        chunk_size = 512
        offset = 0
        decrypted = b""
        while offset < len(raw_data): # Keep loop going as long as we have chunks to decrypt
            chunk = raw_data[offset: offset + chunk_size] # The current chunk
            decrypted += self.rsa_key.decrypt(chunk) # Append the decrypted chunk to the overall decrypted file
            offset += chunk_size # Increase the offset by chunk size

        with open(file_name, "wb") as wfile: # Write the decrypted contents to a file
            fd.write(zlib.decompress(decrypted))