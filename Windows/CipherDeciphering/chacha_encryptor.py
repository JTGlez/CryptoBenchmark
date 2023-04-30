from Crypto.Cipher import ChaCha20
from os import path

class FileEncryptor_ChaCha20:
    def __init__(self, filename):
        self.key = b'00001111000011110000111100001111' # Llave de 32 bytes
        self.filename = filename
        self.tuple = path.splitext(filename)
        self.name = self.tuple[0]
        self.ext = self.tuple[1]

    def cipher(self):
        with open(self.filename, "rb") as file:
            archivo = file.read()

        cipher = ChaCha20.new(key=self.key)
        self.nonce = cipher.nonce
        ciphertext = cipher.encrypt(archivo)

        cipherFile = self.name + '_ChaCha20.bin'
        with open(cipherFile, "wb") as newFile:
            newFile.write(ciphertext)

        return ciphertext

    def decipher(self):
        with open(self.name + '_ChaCha20.bin', "rb") as file:
            ciphertext = file.read()

        decipher = ChaCha20.new(key=self.key, nonce=self.nonce)
        decrypted_file = decipher.decrypt(ciphertext)

        descipherFile = self.name + '_ChaCha20_desc' + self.ext
        with open(descipherFile, "wb") as newFile:
            newFile.write(decrypted_file)

        return decrypted_file
