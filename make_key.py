#pip install pycrypto
#Python 2.7
import os

key = os.urandom(32)
print "Key: " + str(key)
print "Length: " + str(len(key))
with open('key.bin', 'wb') as keyfile:
        keyfile.write(str(key))
keyfile.close()
