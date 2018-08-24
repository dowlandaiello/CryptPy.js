from Crypto.PublicKey import RSA
import hashlib, random

def sha256(s):
    sig = hashlib.sha256(s.encode()).hexdigest()
    return sig

class Key():
    def __init__(self, size): # Generate a new RSA key size 2048
        self.key = RSA.generate(size, e=65537) # Generate a public/ private key pair using 4096 bits key length (512 bytes)
        self.private_key = self.key.exportKey("PEM") # The private key in PEM
        self.public_key = self.key.publickey().exportKey("PEM") # The public key in PEM
        self.key_name = sha256(str(random.random()))[:5]
    def export_keys(self):
        with open("keys/private_" + self.key_name + ".pem", "wb") as wfile:
            wfile.write(self.private_key)
        with open("keys/public_" + self.key_name + ".pem", "wb") as wfile:
            wfile.write(self.public_key)
