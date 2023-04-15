#RSA - Probabilistic Signature Scheme
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

#----------------------PROCESO DE GENERACIÓN Y EXPORTACIÓN DE CLAVES-------------------------#

#Guarda el par de claves generadas en ficheros.
def guardarKeys(private_key, public_key):
    with open("private.pem", "wb") as f:
        f.write(private_key)
    with open("public.pem", "wb") as f:
        f.write(public_key) 

#Generación de pareja de claves RSA de 2048 bits. Se usa un vector de inicialización.
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)

#Passphrase para el cifrado de la clave privada.
passphrase = "12345"

#Exportación de la clave privada.
private_key = key.export_key(passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")

#Cálculo de la clave pública.
public_key = key.publickey().export_key()


#----------------------------PROCESO DE FIRMADO Y VERIFICACIÓN--------------------------------#
#Definición del mensaje a verificar.
message = b'To be signed'
#Recuperamos la clave privada del archivo de seguridad.
key_private = RSA.import_key(open('private.pem').read(), passphrase)
#Cálculo de un hash para el firmado con SHA-256.
hash = SHA256.new(message)
#Firmado del mensaje.
signature = pss.new(key_private).sign(hash)

#Leemos la claves publica generada previamente, obtenemos el hash del mensaje a verificar.
key_public = RSA.import_key(open('public.pem').read(), passphrase)
hash = SHA256.new(message)
verifier = pss.new(key_public)

#Try-Catch para verificar si la firma es válida. Si no, lanza una excepción.
try:
    verifier.verify(hash, signature)
    print("La firma del archivo es válida.")
except (ValueError, TypeError):
    print("La firma del archivo es incorrecta y ha sido alterada.")