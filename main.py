#Importación de bibliotecas.
import subprocess
import sys

#Instalación de paquetes en el environment de ejecución.
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


#Instalación de bibliotecas adicionales.
install('pycryptodome')
install('matplotlib')
install('ecdsa')
install('cryptography')

#Ejecución de los scripts.
subprocess.call(['python','./run_Benchmark.py'])
