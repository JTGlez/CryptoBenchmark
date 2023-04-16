from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64

#----------------------PROCESO DE GENERACIÓN Y EXPORTACIÓN DE CLAVES-------------------------#
def generate_pk():
    """Genera la clave privada para el firmado con Ed25519."""

    # Generación de una clave privada aleatoria sobre la curva 25519.
    private_key = Ed25519PrivateKey.generate()

    # Passphrase para cifrar la clave privada generada.
    frase = "ProyectoCrypto123_!ñ"

    # Exportación de la clave privada a un archivo en formato .pem
    with open("Signing/private_key_ed25519.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(frase.encode())
        ))

    return frase

#---------------------------PROCESO DE FIRMADO Y VERIFICACIÓN---------------------------------#
def signing(file):
    """Realiza el proceso de firma y verificación de la firma sobre un archivo vector de prueba con Ed25519."""

    # Genera la clave privada sobre la curva Ed25519, recupera el passphrase.
    #frase = generate_pk()
    frase = "ProyectoCrypto123_!ñ"

    # Apertura del archivo a firmar en formato binario.
    with open(file, "rb") as imageFile:
        archivo = imageFile.read()

    # Apertura de la clave privada desde el archivo exportado.
    with open("Signing/private_key_ed25519.pem", "rb") as f:
        private_key_bytes = f.read()
        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=frase.encode()
        )

    # Firmado del archivo.
    signature = private_key.sign(archivo)

    # Generación de la clave pública a partir de la clave privada.
    public_key = private_key.public_key()

    # Verificación de firma legítima o apócrifa.
    try:
        public_key.verify(signature, archivo)
        #print(base64.b64encode(signature))
        print("Firma auténtica y validada con Ed25519.")
    except (ValueError, TypeError):
        print("Firma inválida.")