#Python 2.7
import os

iv = os.urandom(16)
print "Initialization Vector: " + str(iv)
print "Length: " + str(len(iv))
with open('iv.bin', 'wb') as ivfile:
        ivfile.write(str(iv))
ivfile.close()
