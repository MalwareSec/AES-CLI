#Python 2.7
#Command line AES Encryption Program
#Twitter: @malware_sec
from Crypto.Cipher import AES
import base64

BLOCK_SIZE=16
def encode(message):
    while len(message) % 16 != 0:
        message += '\x00'
    with open('key.bin', 'rb') as keyfile:
        key = keyfile.read()
        keyfile.close()
    with open('iv.bin', 'rb') as ivfile:
        iv = ivfile.read()
        ivfile.close()
    cipher = AES.new(str(key), AES.MODE_CBC, str(iv))
    cipher_text = base64.b64encode(iv + cipher.encrypt(message))
    return cipher_text

def decode(crypt):
    message = encode(crypt)
    msg = base64.b64decode(message)
    with open('key.bin', 'rb') as keyfile:
        key = keyfile.read()
        keyfile.close()
    iv = msg[:BLOCK_SIZE]
    cipher = AES.new(str(key), AES.MODE_CBC, iv)
    return cipher.decrypt(msg[BLOCK_SIZE:])

def main():
    message = raw_input("Enter message you want to encrypt: ")
    encrypted_text = encode(message)
    print encrypted_text
    decrypted_text = decode(message)
    print decrypted_text

if __name__ == '__main__':
    main()
