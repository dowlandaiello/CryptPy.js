from Crypto.PublicKey import RSA
import hashlib, random, os

def sha256(s):
    sig = hashlib.sha256(s.encode()).hexdigest()
    return sig

class Key():
    def __init__(self): # Generate a new RSA key size 2048
        self.key = None
        self.private_key = None
        self.public_key = None
        self.key_name = None
    def load_public(self, key_hash): # load a public key
        try:
            with open("key/" + key_hash + "/public_" + key_hash + ".pem", "rb") as rfile:
                self.public_key = rfile.read()
            return self.public_key
        except Exception as e:
            print("error loading public key '" + key_hash + "'")
            print(e)
    def load_private(self, key_hash): # load a private key
        try:
            with open("key/" + key_hash + "/private_" + key_hash + ".pem", "rb") as rfile:
                self.public_key = rfile.read()
            return self.public_key
        except Exception as e:
            print("error loading private key '" + key_hash + "'")
            print(e)
    def new_key(self, size): # generate a new key
        self.key = RSA.generate(size, e=65537) # Generate a public/ private key pair using 4096 bits key length (512 bytes)
        self.private_key = self.key.exportKey("PEM") # The private key in PEM
        self.public_key = self.key.publickey().exportKey("PEM") # The public key in PEM
        self.key_name = sha256(str(random.random()))[:7] # create a random key name
        self.export_keys()
    def export_keys(self): # export the new key to the key folder
        directory = "key/" + self.key_name
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            print("that key already exists")
            return 1
        with open("key/" + self.key_name + "/private_" + self.key_name + ".pem", "wb") as wfile:
            wfile.write(self.private_key)
        with open("key/" + self.key_name + "/public_" + self.key_name + ".pem", "wb") as wfile:
            wfile.write(self.public_key)