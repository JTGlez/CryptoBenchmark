<h1 align="center"> CryptoBenchmark :lock_with_ink_pen:	 </h1>

<img src="https://user-images.githubusercontent.com/68305096/233253614-1d3ba0df-d5a3-4f4d-87e3-4706f3137992.PNG">

# Introducción


CryptoBenchmark es un proyecto desarrollo dentro de la asignatura de Criptografía de la FI UNAM. Consiste en la implementación de los siguientes algoritmos de cifrado, descifrado, hasheo y firma digital:

* Cifrado/Descifrado 

| Algoritmo | Tamaño |
| ------ | ------ |
| Chacha20 |  256 bits |
| AES-EBC | 256 bits |
| AES-GCM | 256 bits |
| RSA-OAEP | 2048 bits |

* Hasheo 

| Algoritmo | Tamaño |
| ------ | ------ |
| SHA-2 | 512 bits |
| SHA-3 | 512 bits |
| Scrypt | Output 32 bits |

* Firmado

| Algoritmo | Tamaño |
| ------ | ------ |
| RSA-PSS | 2048 bits |
| ECDSA P521 | 521 Bits (secp521r1) |
| EdDSA | 32 Bits (Ed25519) |


## 📋 Requerimientos

- Python 3.6 o superior
- matplotlib
- Crypto
- pycryptodome
- cryptography
- rsa

## 🚀 Funcionamiento

```bash
# Ejecutar el archivo main.py. Este script instalará las dependencias necesarias y ejecutará automáticamente el benchmark.
python main.py

```
Se consideran 3 vectores de prueba consistentes en un archivo.txt, un pdf y una imagen en formato .png, qque se encuentran en la carpeta TestVectors. Estos archivos pueden ser modificables por otros archivos, siempre y cuando contengan el mismo nombre. 

```python
archivoTXT = 'TestVectors/text.txt'
archivoPDF = 'TestVectors/file.pdf'
archivoIMG = 'TestVectors/img.png'
```

Si desea añadir otros archivos de distinta naturaleza, modifique la ruta del archivo en los scripts run_Benchmark y run_Signature.

## Autores

- [David Jiménez](https://github.com/Derek533z)
- [Leonardo Cruz](https://github.com/chow-chow)
- [Jorge González](https://github.com/JTGlez)
