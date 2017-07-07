#Python 2.7
import os, hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

raw_key = RSA.generate(2048)
private_key = raw_key.exportKey('PEM')
try:
    with open('key.bin', 'wb') as keyfile:
        keyfile.write(str(private_key))
        keyfile.close()
    print "[*] Successfully created an RSA private key"
except:
    print "[*] Error creating your key"
