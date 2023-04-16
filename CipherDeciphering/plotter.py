import matplotlib.pyplot as plt

def plot_results(file, labels, encryption_times, decryption_times, num_executions):
    colors = ['blue', 'green', 'red']

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
