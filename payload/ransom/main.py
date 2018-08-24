from Crypto.PublicKey import RSA
import hashlib

class Key():
    def __init__(self, size): # Generate a new RSA key size 2048
        self.key = RSA.generate(size, e=65537) # Generate a public/ private key pair using 4096 bits key length (512 bytes)
        self.private_key = self.key.exportKey("PEM") # The private key in PEM
        self.public_key = self.key.publickey().exportKey("PEM") # The public key in PEM
        self.key_name = hashlib(random.randnt)
    def export_keys(self):
        
        with open("keys/private_")



fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

print public_key
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()