from Signing import RSA_PSS, ECDSA_P521, ED25519
#import RSA_PSS, ECDSA_P521, ED25519
import time

archivoTXT = '/content/CryptoBenchmark/Windows/TestVectors/text.txt'
archivoPDF = '/content/CryptoBenchmark/Linux/TestVectors/file.pdf'
archivoIMG = '/content/CryptoBenchmark/Linux/TestVectors/img.PNG'

def benchmark_RSA_PSS(archivo):
    """Invoca la función de firmado RSA_PSS sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = RSA_PSS.signing(archivo)
    fin = time.time()
    tiempo_RSA_PSS = (fin - inicio)
    return tiempo_RSA_PSS

def benchmark_ECDSA521(archivo):
    """Invoca la función de firmado ECDSA - NIST P-521  sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = ECDSA_P521.signing(archivo)
    fin = time.time()
    tiempo_ECDSA_P521 = (fin - inicio)
    return tiempo_ECDSA_P521

def benchmark_ED25519(archivo):
    """Invoca la función de firmado ECDSA - NIST P-521  sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = ED25519.signing(archivo)
    fin = time.time()
    tiempo_ED25519 = (fin - inicio)
    return tiempo_ED25519

def signingTime():
    """Ejecuta los benchmarks 100 veces y almacena el tiempo total obtenido para cada uno de ellos."""

    signing_time = []
    benchmark_loop = 100

    # Benchmark para RSA-PSS.
    total_time_RSA_PSS_TXT = 0 
    total_time_RSA_PSS_PDF = 0 
    total_time_RSA_PSS_IMG = 0 

    for i in range(benchmark_loop):
        total_time_RSA_PSS_TXT += benchmark_RSA_PSS(archivoTXT)
        total_time_RSA_PSS_PDF += benchmark_RSA_PSS(archivoPDF)
        total_time_RSA_PSS_IMG += benchmark_RSA_PSS(archivoIMG)
    
    #Almacenamos los tiempos de ejecución para RSA. 0-1-2
    signing_time.append(total_time_RSA_PSS_TXT/benchmark_loop)
    signing_time.append(total_time_RSA_PSS_PDF/benchmark_loop)
    signing_time.append(total_time_RSA_PSS_IMG/benchmark_loop)

    # Benchmark para ECDSA P521-NIST.
    total_time_ECDSA_TXT = 0 
    total_time_ECDSA_PDF = 0 
    total_time_ECDSA_IMG = 0 

    for i in range(benchmark_loop):
        total_time_ECDSA_TXT += benchmark_ECDSA521(archivoTXT)
        total_time_ECDSA_PDF += benchmark_ECDSA521(archivoPDF)
        total_time_ECDSA_IMG += benchmark_ECDSA521(archivoIMG)
    
    #Almacenamos los tiempos de ejecución para ECDSA. 3-4-5
    signing_time.append(total_time_ECDSA_TXT/benchmark_loop)
    signing_time.append(total_time_ECDSA_PDF/benchmark_loop)
    signing_time.append(total_time_ECDSA_IMG/benchmark_loop)

    # Benchmark para Ed25519.
    total_time_ED25519_TXT = 0 
    total_time_ED25519_PDF = 0 
    total_time_ED25519_IMG = 0 

    for i in range(benchmark_loop):
        total_time_ED25519_TXT += benchmark_ED25519(archivoTXT)
        total_time_ED25519_PDF += benchmark_ED25519(archivoPDF)
        total_time_ED25519_IMG += benchmark_ED25519(archivoIMG)

    #Almacenamos los tiempos de ejecución para ED25519. 6-7-8
    signing_time.append(total_time_ED25519_TXT/benchmark_loop)
    signing_time.append(total_time_ED25519_PDF/benchmark_loop)
    signing_time.append(total_time_ED25519_IMG/benchmark_loop)

    return signing_time


total_time_RSA_PSS_TXT = 0
total_time_RSA_PSS_PDF = 0
total_time_RSA_PSS_IMG = 0

total_time_RSA_PSS_TXT += benchmark_RSA_PSS(archivoTXT)
total_time_RSA_PSS_PDF += benchmark_RSA_PSS(archivoPDF)
total_time_RSA_PSS_IMG += benchmark_RSA_PSS(archivoIMG)