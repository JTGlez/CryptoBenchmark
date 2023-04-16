from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import path

class FileEncryptorAES_CBC:
    def __init__(self, filename):
        self.BLOCK_SIZE = 16
        self.key = b'00001111000011110000111100001111' # Llave de 32 bytes
        self.iv = b'abcdefghijklmnop' # Vector de inicialización de 16 bytes
        self.filename = filename
        self.tuple = path.splitext(filename)
        self.name = self.tuple[0]
        self.ext = self.tuple[1]

    def cipher(self):
        with open(self.filename, "rb") as file:
            archivo = file.read()

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = cipher.encrypt(pad(archivo, self.BLOCK_SIZE))

        cipherFile = self.name + '_AES_CBC.bin'
        with open(cipherFile, "wb") as newFile:
            newFile.write(ciphertext)

        return ciphertext

    def decipher(self):
        with open(self.name + '_AES_CBC.bin', "rb") as file:
            ciphertext = file.read()

        decipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_file = unpad(decipher.decrypt(ciphertext), self.BLOCK_SIZE)

        descipherFile = self.name + '_AES_CBC_desc' + self.ext
        with open(descipherFile, "wb") as newFile:
            newFile.write(decrypted_file)

        return decrypted_file
