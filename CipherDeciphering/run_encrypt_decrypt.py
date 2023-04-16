import time
import os
from aes_cbc_encryptor import FileEncryptorAES_CBC
from aes_ecb_encryptor import FileEncryptorAES_ECB
from chacha_encryptor import FileEncryptor_ChaCha20
import matplotlib.pyplot as plt

archivos_prueba = ['file.pdf', 'img.PNG', 'text.txt']
num_executions = 5  # Número de veces que se ejecutará cada algoritmo

algoritmos = {
    'AES_CBC': FileEncryptorAES_CBC,
    'AES_ECB': FileEncryptorAES_ECB,
    'ChaCha20': FileEncryptor_ChaCha20
}

colors = ['blue', 'green', 'red']

for file in archivos_prueba:
    print(f"Procesando archivo {file}")
    encryption_times = []
    decryption_times = []
    labels = []

    for name, Algorithm in algoritmos.items():
        labels.append(name)
        total_encryption_time = 0
        total_decryption_time = 0

        for _ in range(num_executions):
            alg = Algorithm(file)

            start_time = time.time()
            alg.cipher()
            elapsed_time_encryption = time.time() - start_time
            total_encryption_time += elapsed_time_encryption

            start_time = time.time()
            alg.decipher()
            elapsed_time_decryption = time.time() - start_time
            total_decryption_time += elapsed_time_decryption

            os.remove(alg.name + '_' + name + '.bin')
            os.remove(alg.name + '_' + name + '_desc' + alg.ext)

        avg_encryption_time = total_encryption_time / num_executions
        avg_decryption_time = total_decryption_time / num_executions

        encryption_times.append(avg_encryption_time)
        decryption_times.append(avg_decryption_time)

    # Graficar tiempos de encriptación
    plt.bar(labels, encryption_times, color=colors)
    plt.xlabel("Algoritmos")
    plt.ylabel("Tiempo promedio (s)")
    plt.title(f'Tiempos promedio de encriptación para {file} ({num_executions} ejecuciones)')
    plt.show()

    # Graficar tiempos de desencriptación
    plt.bar(labels, decryption_times, color=colors)
    plt.xlabel("Algoritmos")
    plt.ylabel("Tiempo promedio (s)")
    plt.title(f'Tiempos promedio de desencriptación para {file} ({num_executions} ejecuciones)')
    plt.show()

