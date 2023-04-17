# Benchmark de algoritmos criptográficos.

# Autores: -Calderón Jiménez David
#          -Cruz Rangel Leonardo Said
#          -Téllez González Jorge Luis

#Importación de bibliotecas.
from Signing import run_Signature
from Hashing import run_Hashing
import subprocess
import matplotlib.pyplot as plt
from CipherDeciphering.run_encrypt_decrypt import generate_results
from .CipherDeciphering.plotter import plot_results


#--------------------------Gráficas de Cifrado-------------------------------------#
archivos_prueba = ['TestVectors/file.pdf', 'TestVectors/img.PNG', 'TestVectors/text.txt']
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
    ax.bar(i*3, signing_times[i*3], color=colores[i])
    ax.text(i*3, signing_times[i*3], "txt", ha='center', va='top', color='white', fontsize=12)
    ax.bar(i*3+1, signing_times[i*3+1], color=colores[i+3])
    ax.text(i*3+1, signing_times[i*3+1], "pdf", ha='center', va='top', color='white', fontsize=12)
    ax.bar(i*3+2, signing_times[i*3+2], color=colores[i+6])
    ax.text(i*3+2, signing_times[i*3+2], "img", ha='center', va='top', color='white', fontsize=12)

# Establecer las etiquetas del eje x
etiquetas = ['RSA-PSS', 'ECDSA P521', 'ED25519']
ax.set_xticks([0.5, 3.5, 6.5])
ax.set_xticklabels(etiquetas)

# Ajustar los límites del eje x
ax.set_xlim([-0.5, 8.5])

# Etiqueta del eje y
ax.set_ylabel('Tiempo (segundos)')

# Título de la gráfica
ax.set_title('Tiempo de ejecución para diferentes algoritmos de firma')

# Ajustar el tamaño de la figura
fig.set_size_inches(10, 6)

print(signing_times)
# Mostrar la gráfica
plt.show()

#--------------------------Gráficas de Hashing (archivos)-------------------------------------#
hashing_times = run_Hashing.hashingTime()

# Colores de las barras
colores = ['red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'green', 'green']

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar las barras
for i in range(4):
    ax.bar(i*3, hashing_times[i*3], color=colores[i])
    ax.text(i*3, hashing_times[i*3], "txt", ha='center', va='top', color='white', fontsize=12)
    ax.bar(i*3+1, hashing_times[i*3+1], color=colores[i+4])
    ax.text(i*3+1, hashing_times[i*3+1], "pdf", ha='center', va='top', color='white', fontsize=12)
    ax.bar(i*3+2, hashing_times[i*3+2], color=colores[i+8])
    ax.text(i*3+2, hashing_times[i*3+2], "img", ha='center', va='top', color='white', fontsize=12)


# Establecer las etiquetas del eje x
etiquetas = ['SHA-2 384', 'SHA-2 512', 'SHA-3 384', 'SHA-3 512']
ax.set_xticks([1.0, 4.0, 7.0, 10.0])
ax.set_xticklabels(etiquetas)

# Ajustar los límites del eje x
ax.set_xlim([-0.5, 11.5])

# Etiqueta del eje y
ax.set_ylabel('Tiempo de hashing (segundos)')

# Título de la gráfica
ax.set_title('Tiempo de ejecución para diferentes algoritmos de hash')

# Ajustar el tamaño de la figura
fig.set_size_inches(10, 6)

print(hashing_times)

# Mostrar la gráfica
plt.show()

#--------------------------Gráficas de Hashing (contraseñas)-------------------------------------#
password = b'ProyectoCrypto123_!'
password_times = run_Hashing.hash_password(password)

algorithms = ['SHA2-384', 'SHA2-512', 'SHA3-384', 'SHA3-512', 'Scrypt']

print(password_times)

plt.figure(figsize=(10, 6))
plt.bar(algorithms, password_times)
plt.ylabel('Tiempo (segundos): Escala logarítmica')
plt.title('Tiempos de ejecución para la contraseña: "ProyectoCrypto123_!"')
plt.yscale('log')
plt.show()
