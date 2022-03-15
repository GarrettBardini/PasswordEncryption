###############################################################
#####     PASSWORD ENCRYPTION: FERNET                     #####
#####     AUTHOR: GARRETT PETER BARDINI (GPB)             #####
#####     CREATE_DATE: 2021/03/14                         #####
#####     LAST_MODIFIED: 2021/03/28                       #####
###############################################################
import os
from cryptography.fernet import Fernet

class Crypt:
    def __init__(self,WorkingDir):
        WorkingDir = WorkingDir
        os.chdir(WorkingDir)
    def write_key():
        key = Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(key)
    def load_key():
        return open("key.key", "rb").read()
    def write_hash():
        encrypted = encryption_key.encrypt(plain_text_password)
        with open ("pass.key", "wb") as write_hash:
            write_hash.write(encrypted)
    def load_hash():
        return open("pass.key", "rb").read()
    def decrypt():
        return encryption_key.decrypt(encrypted_password).decode("utf-8")

if __name__ == "__main__":
    WorkingDir = (os.path.dirname(os.path.realpath(__file__)))
    if os.path.isfile(os.path.join(WorkingDir,"pass.key")) == True & os.path.isfile(os.path.join(WorkingDir,"key.key")) == True:
        Crypt(WorkingDir)
        key = Crypt.load_key()
        encryption_key = Fernet(key)
        encrypted_password = Crypt.load_hash()
        decrypted_password = Crypt.decrypt()
    else:
        plain_text_password = input("Enter the password you would like to encrypt and store:\n").encode()
        Crypt(WorkingDir)
        Crypt.write_key()
        key = Crypt.load_key()
        encryption_key = Fernet(key)
        Crypt.write_hash()
        encrypted_password = Crypt.load_hash()
        decrypted_password = Crypt.decrypt()
    print(decrypted_password)