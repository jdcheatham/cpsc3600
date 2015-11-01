__author__ = 'j'

import os
import binascii
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = binascii.unhexlify(b'd984ab2d70fab1c954479a9a51ca301e5fd490d0432c080f3cfc979e3bbe7a7d')
salt = ('bf5c8c73bac23e156421cd5fdedbc818')
fin = open ('word8')
for word in fin:
    word=word.strip()
    word=word.lower()
    password_bytes = word.encode(encoding='UTF-8')
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=binascii.unhexlify(salt),
            iterations=100000,
            backend=backend
        )
        kdf.verify(password_bytes,key)
        print(word+' this worked')
        break

    except:
        print(word+" didn't work")
fin.close()
def main():

    if __name__ == "__main__":
     main()