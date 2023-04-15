from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64

#---------------------------PROCESO DE FIRMADO Y VERIFICACIÓN---------------------------------#
def signing(file):
    """Realiza el proceso de firma y verificación de la firma sobre un archivo vector de prueba."""

     # Generación de una clave privada aleatoria sobre curva elíptica secp521r1.
    private_key = ec.generate_private_key(ec.SECP521R1())

    # Apertura del archivo a firmar en formato binario.
    with open(file, "rb") as imageFile:
        archivo = imageFile.read()

    # Firmado del archivo.
    signature = private_key.sign(archivo, ec.ECDSA(hashes.SHA256()))

    # Verificación de firma legítima o apócrifa.
    try:
        public_key = private_key.public_key()
        public_key.verify(signature, archivo, ec.ECDSA(hashes.SHA256()))
        print(base64.b64encode(signature))
        print ("Firma auténtica y validada.")
    except (ValueError, TypeError):
        print ("Firma inválida.")