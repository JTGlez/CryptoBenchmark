# Benchmark de algoritmos criptográficos.

# Autores: -Calderón Jiménez David
#          -Cruz Rangel Leonardo Said
#          -Téllez González Jorge Luis

#Importación de bibliotecas.
from Signing import run_Signature
import subprocess
import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')


#--------------------------Gráficas de Firmado-------------------------------------
signing_times = run_Signature.signingTime()

fig, ax = plt.subplots()
algoritmos = ['RSA-PSS', 'ECDSA P521', 'ED25519']
tiempos = signing_times
tiempos_labels = [round(time_RSA_PSS,2), round(time_ECDSA_PRIME,2), round(time_ECDSA_BINARY,2)]
bar_colors = ['red', 'blue', 'green']

ax.bar(algoritmos, tiempos, color=bar_colors)
addlabels(algoritmos, tiempos_labels)
ax.set_ylabel('Time in milliseconds')
ax.set_title('Execution time of signature algorithms')

plt.show()
