import time
import os
from aes_cbc_encryptor import FileEncryptorAES_CBC
from aes_ecb_encryptor import FileEncryptorAES_ECB
from chacha_encryptor import FileEncryptor_ChaCha20
import matplotlib.pyplot as plt

archivos_prueba = ['file.pdf', 'img.PNG', 'text.txt']

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
        alg = Algorithm(file)

        start_time = time.time()
        alg.cipher()
        elapsed_time_encryption = time.time() - start_time

        start_time = time.time()
        alg.decipher()
        elapsed_time_decryption = time.time() - start_time

        encryption_times.append(elapsed_time_encryption)
        decryption_times.append(elapsed_time_decryption)

        os.remove(alg.name + '_' + name + '.bin')
        os.remove(alg.name + '_' + name + '_desc' + alg.ext)

    # Graficar tiempos de encriptación
    plt.bar(labels, encryption_times, color=colors)
    plt.xlabel("Algoritmos")
    plt.ylabel("Tiempo (s)")
    plt.title(f'Tiempos de encriptación para {file}')
    plt.show()

    # Graficar tiempos de desencriptación
    plt.bar(labels, decryption_times, color=colors)
    plt.xlabel("Algoritmos")
    plt.ylabel("Tiempo (s)")
    plt.title(f'Tiempos de desencriptación para {file}')
    plt.show()

