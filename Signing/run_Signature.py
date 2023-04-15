import RSA_PSS
import matplotlib.pyplot as plt
import time

archivo = 'TestVectors/text.txt'

def benchmarkRSA_PSS():
    """Invoca el método de firmado RSA_PSS sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    firmado = RSA_PSS.signing(archivo)
    fin = time.time()
    tiempo_RSA_PSS = (fin - inicio)
    return tiempo_RSA_PSS






rsa_pss_time = benchmarkRSA_PSS()
print("Tiempo de RSA-PSS con el vector de prueba: ", rsa_pss_time, "segundos.")