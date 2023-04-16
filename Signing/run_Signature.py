import RSA_PSS, ECDSA_P521, ED25519
import time

archivoTXT = 'TestVectors/text.txt'
archivoPDF = 'TestVectors/file.pdf'
archivoIMG = 'TestVectors/img.png'

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

    # Benchmark para RSA-PSS.
    total_time_RSA_PSS_TXT = 0 
    total_time_RSA_PSS_PDF = 0 
    total_time_RSA_PSS_IMG = 0 

    for i in range(100):
        total_time_RSA_PSS_TXT += benchmark_RSA_PSS(archivoTXT)
        total_time_RSA_PSS_PDF += benchmark_RSA_PSS(archivoPDF)
        total_time_RSA_PSS_IMG += benchmark_RSA_PSS(archivoIMG)
    
    #Almacenamos los tiempos de ejecución para RSA. 0-1-2
    signing_time.append(total_time_RSA_PSS_TXT/100)
    signing_time.append(total_time_RSA_PSS_PDF/100)
    signing_time.append(total_time_RSA_PSS_IMG/100)

    # Benchmark para ECDSA P521-NIST.
    total_time_ECDSA_TXT = 0 
    total_time_ECDSA_PDF = 0 
    total_time_ECDSA_IMG = 0 

    for i in range(100):
        total_time_ECDSA_TXT += benchmark_ECDSA521(archivoTXT)
        total_time_ECDSA_PDF += benchmark_ECDSA521(archivoPDF)
        total_time_ECDSA_IMG += benchmark_ECDSA521(archivoIMG)
    
    #Almacenamos los tiempos de ejecución para ECDSA. 3-4-5
    signing_time.append(total_time_ECDSA_TXT/100)
    signing_time.append(total_time_ECDSA_PDF/100)
    signing_time.append(total_time_ECDSA_IMG/100)

    # Benchmark para Ed25519.
    total_time_ED25519_TXT = 0 
    total_time_ED25519_PDF = 0 
    total_time_ED25519_IMG = 0 

    for i in range(100):
        total_time_ED25519_TXT += benchmark_ED25519(archivoTXT)
        total_time_ED25519_PDF += benchmark_ED25519(archivoPDF)
        total_time_ED25519_IMG += benchmark_ED25519(archivoIMG)

    #Almacenamos los tiempos de ejecución para ED25519. 6-7-8
    signing_time.append(total_time_ED25519_TXT/100)
    signing_time.append(total_time_ED25519_PDF/100)
    signing_time.append(total_time_ED25519_IMG/100)

    return signing_time

signingTiming = signingTime()
print(signingTiming)