import os
import matplotlib.pyplot as plt

def plot_results(file, labels, encryption_times, decryption_times, num_executions):
    colors = ['blue', 'green', 'red']
    x = range(len(labels))

    file_name = os.path.basename(file)  # Extraer solo el nombre del archivo

    fig, ax = plt.subplots(1, 3, figsize=(20, 5), sharey=True)

    for i in range(len(labels)):
        # Graficar tiempos de encriptación
        ax[i].bar(0, encryption_times[i], color=colors[i])
        ax[i].set_xlabel("Cifrado")

        # Graficar tiempos de desencriptación
        ax[i].bar(1, decryption_times[i], color=colors[i])
        ax[i].set_xlabel("Descifrado")

        ax[i].set_xticks([0, 1])
        ax[i].set_xticklabels(["Cifrado", "Descifrado"])
        ax[i].set_title(f'{labels[i]} para {file_name} ({num_executions} ejecuciones)')

    ax[0].set_ylabel("Tiempo promedio (s)")
    plt.show()
