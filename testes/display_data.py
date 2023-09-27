import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def init_heatmap():
    # Função para inicializar o gráfico de calor
    data = np.zeros((8, 8))
    cax = plt.imshow(data, cmap='rainbow',
                     interpolation='nearest', vmin=0, vmax=1)
    plt.colorbar(cax)
    return cax


def update_heatmap(frame, cax):
    data = asdad
    cax.set_data(data)
    plt.title('Gráfico de Calor em Tempo Real')


# Configuração inicial do gráfico
fig, ax = plt.subplots()

# Inicializa o gráfico de calor
cax = init_heatmap()

# Configuração da animação
ani = FuncAnimation(fig, update_heatmap, fargs=(
    cax,), interval=1000)  # Atualiza a cada 1 segundo

plt.show()
