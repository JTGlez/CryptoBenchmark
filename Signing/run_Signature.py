from Signing import RSA_PSS
import matplotlib.pyplot as plt
import time

archivo = 'TestVectors/text.txt'

def benchmarkRSA_PSS():
    """Invoca el método de firmado RSA_PSS sobre un archivo vector de prueba y mide el tiempo de prueba."""
    inicio = time.time()
    RSA_PSS = RSA_PSS.signing(archivo)
    fin = time.time()
    tiempo_RSA_PSS = (fin - inicio) * 1000
    return tiempo_RSA_PSS