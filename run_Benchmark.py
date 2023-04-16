# Benchmark de algoritmos criptográficos.

# Autores: -Calderón Jiménez David
#          -Cruz Rangel Leonardo Said
#          -Téllez González Jorge Luis

# Importación de bibliotecas.
from Signing import run_Signature
from CipherDeciphering.results_generator import generate_results
from CipherDeciphering.plotter import plot_results

archivos_prueba = ['file.pdf', 'img.PNG', 'text.txt']
num_executions = 5

for file in archivos_prueba:
    print(f"Procesando archivo {file}")
    labels, encryption_times, decryption_times = generate_results(file, num_executions)
    plot_results(file, labels, encryption_times, decryption_times, num_executions)

signing_times = run_Signature.signingTime()
