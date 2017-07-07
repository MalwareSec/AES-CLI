#Python 2.7
#Command line AES Encryption Program
#Twitter: @malware_sec
#Python 2.7
import os, base64, hashlib
from Crypto import Random
from Crypto.Cipher import AES

with open("key.bin", "rb") as keyfile:
	key = keyfile.read()

hash_key = hashlib.sha256(key.encode()).digest()

def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_b64(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    b64_cipher = base64.b64encode(iv + cipher.encrypt(message))
    return b64_cipher

def decrypt_b64(ciphertext, key):
    message = base64.b64decode(ciphertext)
    iv = message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(message[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt(message, key, key_size=356):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = (iv + cipher.encrypt(message))
    return cipher_text

def decrypt(message, key):
    iv = message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(message[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as unencypted_file:
        plaintext = unencypted_file.read()
    crypt = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(crypt)
    #Option to delete the original file
    #option = raw_input("Do you want to delete the original file?[Y/N]: ")
    #if option == "Y" or option == "y":
    os.remove(file_name)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as encrypted_file:
        ciphertext = encrypted_file.read()
    crypt = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as encrypted_file:
        encrypted_file.write(crypt)

def main():
    ext = [".txt"] #Add other extensions as needed
    files_to_enc = [] #Array of all found extensions
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.getcwd()
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(tuple(ext)):
                files_to_enc.append(os.path.join(root, file))
    print "Encrypting all files in directory " + str(dir_path)
    print "Encrypting files: " + str(files_to_enc)
    for files in files_to_enc:
        encrypt_file(files, hash_key)
    print "[!] Encryption Done"
    decode_file = raw_input("Do you want to decode your file? [Y/N]: ")
    if decode_file == "Y" or decode_file == "y":
        ext = [".enc"]
        files_to_dec = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(tuple(ext)):
                    files_to_dec.append(os.path.join(root, file))
        print "Decrypting all files in directory " + str(dir_path)
        print "Decrypting files: " + str(files_to_dec)
        for files in files_to_dec:
            decrypt_file(files, hash_key)
        print "[!] Decryption Done"

if __name__ == "__main__":
    main()
