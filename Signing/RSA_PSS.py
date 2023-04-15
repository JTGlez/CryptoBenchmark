#RSA - Probabilistic Signature Scheme
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

#----------------------PROCESO DE GENERACIÓN Y EXPORTACIÓN DE CLAVES-------------------------#
def generate_keys():
    """Genera el par de claves (pública y privada) para el firmado con RSA-PSS. """

    # Generación del par de claves.
    key = RSA.generate(2048)

    # Passphrase para cifrar la clave privada generada.
    frase = "ProyectoCrypto123_!ñ"

    # Exportación de la clave privada al archivo private.pem. Abre el archivo private.pem, y lo crea si es que no existe.
    private_key = key.export_key(passphrase = frase)
    with open("private.pem", "wb") as f:
        f.write(private_key)
    
    # Exportación de la clave pública al archivo public.pem. Abre el archivo public.pem, y lo crea si es que no existe.
    public_key = key.publickey().export_key()
    with open("public.pem", "wb") as f:
        f.write(public_key)

    return frase

#---------------------------PROCESO DE FIRMADO Y VERIFICACIÓN---------------------------------#

def signing(file):
    """Realiza el proceso de firma y verificación de la firma sobre un archivo vector de prueba."""

    # Se obtiene el par de claves con la función generate_keys y sus correspondientes archivos en formato .pem. Se recupera la passphrase.
    frase = generate_keys()

    # Apertura del archivo a firmar en formato binario.
    with open(file, "rb") as imageFile:
        archivo = imageFile.read()

    # Proceso de firmado con la clave privada con cálculo de hash.
    privatekey = RSA.import_key(open('private.pem').read(), frase)
    hash = SHA256.new(archivo)
    firma = pss.new(privatekey).sign(hash)

    # Proceso de verificación de la firma con la clave pública del firmante.
    publickey = RSA.import_key(open('public.pem').read())
    hash = SHA256.new(archivo)
    verificador = pss.new(publickey)

    # Verificación de firma legítima o apócrifa.
    try:
        verificador.verify(hash, firma)
        print ("Firma auténtica y validada.")
    except (ValueError, TypeError):
        print ("Firma inválida.")