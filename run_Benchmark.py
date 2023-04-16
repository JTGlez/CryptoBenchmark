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


#--------------------------Gráficas de Cifrado-------------------------------------#

archivos_prueba = ['file.pdf', 'img.PNG', 'text.txt']
num_executions = 5

for file in archivos_prueba:
    print(f"Procesando archivo {file}")
    labels, encryption_times, decryption_times = generate_results(file, num_executions)
    plot_results(file, labels, encryption_times, decryption_times, num_executions)


#--------------------------Gráficas de Firmado-------------------------------------#
signing_times = run_Signature.signingTime()

# Colores de las barras
colores = ['red', 'red', 'red', 'blue', 'blue', 'blue', 'green', 'green', 'green']

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar las barras
for i in range(3):
    ax.bar(i*3, signing_times[i], color=colores[i])
    ax.bar(i*3+1, signing_times[i+3], color=colores[i+3])
    ax.bar(i*3+2, signing_times[i+6], color=colores[i+6])

# Establecer las etiquetas del eje x
etiquetas = ['RSA-PSS', 'ECDSA P521', 'ED25519']
ax.set_xticks([0.5, 3.5, 6.5])
ax.set_xticklabels(etiquetas)

# Ajustar los límites del eje x
ax.set_xlim([-0.5, 8.5])


# Mostrar la gráfica
plt.show()