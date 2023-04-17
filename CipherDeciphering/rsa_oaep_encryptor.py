from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from os import path

class FileEncryptor_RSA_OAEP:
    def __init__(self, filename):
        self.key = RSA.generate(2048)
        self.publicKey = self.key.publickey()
        self.filename = filename
        self.tuple = path.splitext(filename)
        self.name = self.tuple[0]
        self.ext = self.tuple[1]

    def cipher(self):
        with open(self.filename, "rb") as file:
            archivo = file.read()

        cipher = PKCS1_OAEP.new(key=self.publicKey)
        self.nonce = cipher.nonce
        ciphertext = cipher.encrypt(archivo)

        cipherFile = self.name + '_RSA_OAEP.bin'
        with open(cipherFile, "wb") as newFile:
            newFile.write(ciphertext)

        return ciphertext

    def decipher(self):
        with open(self.name + '_RSA_OAEP.bin', "rb") as file:
            ciphertext = file.read()

        decipher = PKCS1_OAEP.new(key=self.key, nonce=self.nonce)
        decrypted_file = decipher.decrypt(ciphertext)

        descipherFile = self.name + '_RSA_OAEP_desc' + self.ext
        with open(descipherFile, "wb") as newFile:
            newFile.write(decrypted_file)

        return decrypted_file