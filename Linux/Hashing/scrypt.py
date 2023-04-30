from Crypto.Protocol.KDF import scrypt
import time

# Scrypt es una función de derivación de clave (KDF, por sus siglas en inglés)
# Está basada en hash y fue diseñada para ser resistente a los ataques de
# fuerza bruta.

# Es común y ampliamente utilizada para almacenar contraseñas de usuario
# de forma segura así como para generar claves de cifrado y autenticación
# en aplicaciones que requieren alta seguridad.

def benchmark(password):
    """Mide el tiempo de ejecución para una contraseña dada"""
    salt = b'My salt'
    start = time.time()
    scrypt(password, salt=salt, N = 2**14, r = 8, p = 1, key_len=32)
    end = time.time()
    return end - start
