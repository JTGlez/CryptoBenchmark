# Benchmark de algoritmos criptográficos.

# Autores: -Calderón Jiménez David
#          -Cruz Rangel Leonardo Said
#          -Téllez González Jorge Luis

#Importación de bibliotecas.
from Signing import run_Signature
import os
from Hashing import run_Hashing
import subprocess
import matplotlib.pyplot as plt
from CipherDeciphering.run_encrypt_decrypt import generate_results,generate_rsa_results
from CipherDeciphering.plotter import plot_results


#--------------------------Gráficas de Cifrado-------------------------------------#
archivos_prueba = ['/content/CryptoBenchmark/Linux/TestVectors/file.pdf', '/content/CryptoBenchmark/Linux/TestVectors/img.PNG', '/content/CryptoBenchmark/Linux/TestVectors/text.txt']
num_executions = 100

y = 0
for file in archivos_prueba:
    y = y + 1
    print(f"Procesando archivo {file}")
    labels, encryption_times, decryption_times = generate_results(file, num_executions)
    colors = ['blue', 'green', 'red']

    file_name = os.path.basename(file)  # Extraer solo el nombre del archivo

    fig, ax = plt.subplots(1, 3, figsize=(20, 5), sharey=True)

    for i in range(len(labels)):
        # Graficar tiempos de cifrado
        ax[i].bar(0, encryption_times[i], color=colors[i])
        ax[i].set_xlabel("Cifrado")

        # Graficar tiempos de descifrado
        ax[i].bar(1, decryption_times[i], color=colors[i])
        ax[i].set_xlabel("Descifrado")

        ax[i].set_xticks([0, 1])
        ax[i].set_xticklabels(["Cifrado", "Descifrado"])
        ax[i].set_title(f'{labels[i]} para {file_name} ({num_executions} ejecuciones)')

    ax[0].set_ylabel("Tiempo promedio (s)")
    plt.savefig('ciphertest{}.png'.format(y), dpi=300)
    plt.show()

print(f"Procesando archivo text.txt")
labels, encryption_times, decryption_times = generate_rsa_results('/content/CryptoBenchmark/Linux/TestVectors/text.txt', num_executions)
colors = ['blue', 'green', 'red']

file_name = 'text.txt'  # Extraer solo el nombre del archivo

fig, ax = plt.subplots(figsize=(20, 5), sharey=True)

for i in range(len(labels)):
    # Graficar tiempos de cifrado
    ax.bar(0, encryption_times[i], color=colors[i])
    ax.set_xlabel("Cifrado")

    # Graficar tiempos de descifrado
    ax.bar(1, decryption_times[i], color=colors[i])
    ax.set_xlabel("Descifrado")

    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Cifrado", "Descifrado"])
    ax.set_title(f'{labels} para {file_name} ({num_executions} ejecuciones)')

ax.set_ylabel("Tiempo promedio (s)")
plt.savefig('ciphertest4.png', dpi=300)
plt.show()


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
plt.savefig('firmatest.png', dpi=300)
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
plt.savefig('hashtest.png', dpi=300)
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
