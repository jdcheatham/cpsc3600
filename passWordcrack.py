"""Pasword cracker
JD Cheatham
cpsc3600"""

import os
import binascii
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
s=input("Salt")
k=input("key")
backend = default_backend()
#salt = os.urandom(16)
salt = binascii.unhexlify(s)
# derive
"""kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=backend
)
key = kdf.derive(b"password")"""
# verify
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=backend
)
kdf.verify(b"password", binascii.unhexlify(k))
print ('hey this one worked')
print (binascii.hexlify(salt))

def main():

    if __name__ == "__main__":
     main()
