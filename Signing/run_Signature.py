import RSA_PSS, ECDSA_P521, ED25519
import time

archivo = 'TestVectors/text.txt'

def benchmark_RSA_PSS():
    """Invoca la función de firmado RSA_PSS sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = RSA_PSS.signing(archivo)
    fin = time.time()
    tiempo_RSA_PSS = (fin - inicio)
    return tiempo_RSA_PSS

def benchmark_ECDSA521():
    """Invoca la función de firmado ECDSA - NIST P-521  sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = ECDSA_P521.signing(archivo)
    fin = time.time()
    tiempo_ECDSA_P521 = (fin - inicio)
    return tiempo_ECDSA_P521

def benchmark_ED25519():
    """Invoca la función de firmado ECDSA - NIST P-521  sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = ED25519.signing(archivo)
    fin = time.time()
    tiempo_ECDSA_P521 = (fin - inicio)
    return tiempo_ECDSA_P521

rsa_pss_time = benchmark_RSA_PSS()
ecdsa_p521_time = benchmark_ECDSA521()
ed_25519_time = benchmark_ED25519()

print("Tiempo de RSA-PSS con el vector de prueba: ", rsa_pss_time, "segundos.")
print("Tiempo de ECDSA_P521 con el vector de prueba: ", ecdsa_p521_time, "segundos.")
print("Tiempo de ED25519 con el vector de prueba: ", ed_25519_time, "segundos.")