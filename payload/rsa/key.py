from Crypto.PublicKey import RSA
import hashlib, random

def sha256(s):
    sig = hashlib.sha256(s.encode()).hexdigest()
    return sig

class Key():
    def __init__(self): # Generate a new RSA key size 2048
        self.key = None
        self.private_key = None
        self.public_key = None
        self.key_name = None
    def load(self, key_hash): # import a key
        with open("key/public_" + key_hash + ".pem", "rb") as rfile:
            self.public_key = rfile.read()
        return self.public_key

    def new_key(self, size): # generate a new key
        self.key = RSA.generate(size, e=65537) # Generate a public/ private key pair using 4096 bits key length (512 bytes)
        self.private_key = self.key.exportKey("PEM") # The private key in PEM
        self.public_key = self.key.publickey().exportKey("PEM") # The public key in PEM
        self.key_name = sha256(str(random.random()))[:5] # create a random key name
        self.export_keys()
    def export_keys(self): # export the new key to the key folder
        with open("key/private_" + self.key_name + ".pem", "wb") as wfile:
            wfile.write(self.private_key)
        with open("key/public_" + self.key_name + ".pem", "wb") as wfile:
            wfile.write(self.public_key)