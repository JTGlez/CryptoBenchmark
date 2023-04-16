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
    tiempo_ECDSA_P521 = (fin - inicio)
    return tiempo_ECDSA_P521

def signingTime():
    """Ejecuta los benchmarks 100 veces y almacena el tiempo total obtenido para cada uno de ellos."""

    rsa_pss_time = benchmark_RSA_PSS(archivoTXT)
    ecdsa_p521_time = benchmark_ECDSA521(archivoTXT)
    ed_25519_time = benchmark_ED25519(archivoTXT)

    print("Tiempo de RSA-PSS con el vector de prueba: ", rsa_pss_time, "segundos.")
    print("Tiempo de ECDSA_P521 con el vector de prueba: ", ecdsa_p521_time, "segundos.")
    print("Tiempo de ED25519 con el vector de prueba: ", ed_25519_time, "segundos.")
