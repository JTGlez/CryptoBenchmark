from Crypto.Hash import SHA384
import time

def sha2_384(file):
    """Obtiene el Hash de un archivo dado usando SHA-2 384"""
    # Apertura del archivo en modo de lectura binario:
    # Es recomendable dividir el archivo en bloques para archivos grandes,
    # pero como estamos trabajando con archivos pequeños no es necesario.
    with open(file, 'rb') as f:
        data = f.read() # Lee el contenido del archivo en data

    # Creación del objeto SHA-2 384
    sha384 = SHA384.new()

    # Se actualiza el objeto con los datos del archivo
    sha384.update(data)

    # Se retorna el valor del hash en formato hexadecimal
    return sha384.hexdigest()

def benchmark(archivo):
    """Mide el tiempo de ejecución para un archivo de prueba"""
    start = time.time()
    sha2_384(archivo)
    end = time.time()
    return end - start

def benchmark_password(password):
    """Mide el tiempo de ejecución para una contraseña dada"""
    start = time.time()
    hash_object = SHA384.new(password)
    hash_object.hexdigest()
    end = time.time()
    return end - start

