from Hashing import sha2_384, sha2_512, sha3_384, sha3_512, scrypt

archivoTXT = '/content/CryptoBenchmark/Linux/TestVectors/text.txt'
archivoPDF = '/content/CryptoBenchmark/Linux/TestVectors/file.pdf'
archivoIMG = '/content/CryptoBenchmark/Linux/TestVectors/img.PNG'

def hashingTime():
    """Obtiene el tiempo promedio de ejecución de cada algoritmo de hash usando una muestra de 100 ejecuciones"""
    hashing_time = []
    EXEC = 100

    # Para SHA-2 384
    time_sha2_384_txt = 0
    time_sha2_384_pdf = 0
    time_sha2_384_img = 0

    for _ in range(EXEC):
        time_sha2_384_txt += sha2_384.benchmark(archivoTXT)
        time_sha2_384_pdf += sha2_384.benchmark(archivoPDF)
        time_sha2_384_img += sha2_384.benchmark(archivoIMG)

    hashing_time.append(time_sha2_384_txt / EXEC)
    hashing_time.append(time_sha2_384_pdf / EXEC)
    hashing_time.append(time_sha2_384_img / EXEC)

    # Para SHA-2 512
    time_sha2_512_txt = 0
    time_sha2_512_pdf = 0
    time_sha2_512_img = 0

    for _ in range(EXEC):
        time_sha2_512_txt += sha2_512.benchmark(archivoTXT)
        time_sha2_512_pdf += sha2_512.benchmark(archivoPDF)
        time_sha2_512_img += sha2_512.benchmark(archivoIMG)

    hashing_time.append(time_sha2_512_txt / EXEC)
    hashing_time.append(time_sha2_512_pdf / EXEC)
    hashing_time.append(time_sha2_512_img / EXEC)

    # Para SHA-3 384
    time_sha3_384_txt = 0
    time_sha3_384_pdf = 0
    time_sha3_384_img = 0

    for _ in range(EXEC):
        time_sha3_384_txt += sha3_384.benchmark(archivoTXT)
        time_sha3_384_pdf += sha3_384.benchmark(archivoPDF)
        time_sha3_384_img += sha3_384.benchmark(archivoIMG)

    hashing_time.append(time_sha3_384_txt / EXEC)
    hashing_time.append(time_sha3_384_pdf / EXEC)
    hashing_time.append(time_sha3_384_img / EXEC)

    # Para SHA-3 512
    time_sha3_512_txt = 0
    time_sha3_512_pdf = 0
    time_sha3_512_img = 0

    for _ in range(EXEC):
        time_sha3_512_txt += sha3_512.benchmark(archivoTXT)
        time_sha3_512_pdf += sha3_512.benchmark(archivoPDF)
        time_sha3_512_img += sha3_512.benchmark(archivoIMG)

    hashing_time.append(time_sha3_512_txt / EXEC)
    hashing_time.append(time_sha3_512_pdf / EXEC)
    hashing_time.append(time_sha3_512_img / EXEC)

    return hashing_time

def hash_password(password):
    time = []
    EXEC = 100

    time_sha2_384 = 0
    time_sha2_512 = 0
    time_sha3_384 = 0
    time_sha3_512 = 0
    time_scrypt_32 = 0

    for _ in range(EXEC):
        time_sha2_384 += sha2_384.benchmark_password(password)
        time_sha2_512 += sha2_512.benchmark_password(password)
        time_sha3_384 += sha3_384.benchmark_password(password)
        time_sha3_512 += sha3_512.benchmark_password(password)
        time_scrypt_32 += scrypt.benchmark(password)


    time.append(time_sha2_384 / EXEC)
    time.append(time_sha2_512 / EXEC)
    time.append(time_sha3_384 / EXEC)
    time.append(time_sha3_512 / EXEC)
    time.append(time_scrypt_32 / EXEC)

    return time
