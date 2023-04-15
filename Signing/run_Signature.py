import RSA_PSS, ECDSA_P521
import matplotlib.pyplot as plt
import time

archivo = 'TestVectors/text.txt'

def benchmarkRSA_PSS():
    """Invoca la función de firmado RSA_PSS sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = RSA_PSS.signing(archivo)
    fin = time.time()
    tiempo_RSA_PSS = (fin - inicio)
    return tiempo_RSA_PSS

def benchmarkECDSA521():
    """Invoca la función de firmado ECDSA - NIST P-521  sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = ECDSA_P521.signing(archivo)
    fin = time.time()
    tiempo_ECDSA_P521 = (fin - inicio)
    return tiempo_ECDSA_P521

rsa_pss_time = benchmarkRSA_PSS()
ecdsa_p521_time = benchmarkECDSA521()
print("Tiempo de RSA-PSS con el vector de prueba: ", rsa_pss_time, "segundos.")
print("Tiempo de ECDSA_P521 con el vector de prueba: ", ecdsa_p521_time, "segundos.")