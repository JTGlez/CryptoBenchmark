import time
import os
from .aes_cbc_encryptor import FileEncryptorAES_CBC
from .aes_ecb_encryptor import FileEncryptorAES_ECB
from .chacha_encryptor import FileEncryptor_ChaCha20
from .rsa_oaep_encryptor import FileEncryptor_RSA_OAEP

def generate_results(file, num_executions):
    algoritmos = {
        'AES_CBC': FileEncryptorAES_CBC,
        'AES_ECB': FileEncryptorAES_ECB,
        'ChaCha20': FileEncryptor_ChaCha20,
    }

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

    return labels, encryption_times, decryption_times

import time
import os
from .rsa_oaep_encryptor import FileEncryptor_RSA_OAEP

def generate_rsa_results(file, num_executions):
    encryption_times = []
    decryption_times = []
    labels = []

    alg_name = 'RSA_OAEP'
    labels.append(alg_name)
    total_encryption_time = 0
    total_decryption_time = 0

    for _ in range(num_executions):
        alg = FileEncryptor_RSA_OAEP(file)

        start_time = time.time()
        alg.cipher()
        elapsed_time_encryption = time.time() - start_time
        total_encryption_time += elapsed_time_encryption

        start_time = time.time()
        alg.decipher()
        elapsed_time_decryption = time.time() - start_time
        total_decryption_time += elapsed_time_decryption

        os.remove(alg.name + '_' + alg_name + '.bin')
        os.remove(alg.name + '_' + alg_name + '_desc' + alg.ext)

    avg_encryption_time = total_encryption_time / num_executions
    avg_decryption_time = total_decryption_time / num_executions

    encryption_times.append(avg_encryption_time)
    decryption_times.append(avg_decryption_time)

    return labels, encryption_times, decryption_times
