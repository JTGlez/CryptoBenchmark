from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import base64

#----------------------PROCESO DE GENERACIÓN Y EXPORTACIÓN DE CLAVES-------------------------#
def generate_pk():
    """Genera la clave privada para el firmado con ECDSA-P521 NIST. """

    # Generación de una clave privada aleatoria sobre curva elíptica secp521r1.
    private_key = ec.generate_private_key(ec.SECP521R1())

    # Passphrase para cifrar la clave privada generada.
    frase = "ProyectoCrypto123_!ñ"

    # Exportación de la clave privada a un archivo en formato .pem
    with open("Signing/private_key_secp521r1.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(frase.encode())
        ))

    return frase

#---------------------------PROCESO DE FIRMADO Y VERIFICACIÓN---------------------------------#
def signing(file):
    """Realiza el proceso de firma y verificación de la firma sobre un archivo vector de prueba con ECDSA-P521 NIST."""

    # Genera la clave privada sobre un punto de la curva, recupera el passphrase.
    frase = generate_pk()

    # Apertura del archivo a firmar en formato binario.
    with open(file, "rb") as imageFile:
        archivo = imageFile.read()

    # Apertura de la clave privada desde el archivo exportado.
    with open("Signing/private_key_secp521r1.pem", "rb") as f:
        private_key_bytes = f.read()
        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password = frase.encode()
        )

    # Firmado del archivo.
    signature = private_key.sign(archivo, ec.ECDSA(hashes.SHA256()))

    # Generación de la clave pública a partir de la clave privada.
    public_key = private_key.public_key()

    # Verificación de firma legítima o apócrifa.
    try:
        public_key.verify(signature, archivo, ec.ECDSA(hashes.SHA256()))
        #print(base64.b64encode(signature))
        print("Firma auténtica y validada con ECDSA-P521.")
    except (ValueError, TypeError):
        print("Firma inválida.")
