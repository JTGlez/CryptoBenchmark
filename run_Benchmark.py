# Benchmark de algoritmos criptográficos.

# Autores: -Calderón Jiménez David
#          -Cruz Rangel Leonardo Said
#          -Téllez González Jorge Luis

#Importación de bibliotecas.
from Signing import run_Signature
import subprocess
import matplotlib.pyplot as plt
from run_encrypt_decrypt import generate_results
from plotter import plot_results

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')

archivos_prueba = ['file.pdf', 'img.PNG', 'text.txt']
num_executions = 5

for file in archivos_prueba:
    print(f"Procesando archivo {file}")
    labels, encryption_times, decryption_times = generate_results(file, num_executions)
    plot_results(file, labels, encryption_times, decryption_times, num_executions)