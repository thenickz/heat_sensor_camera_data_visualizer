from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import serial

# Inicializa uma matriz vazia para armazenar os dados
heat_matrix = np.zeros((8, 8))


def load_data(ser):
    while True:
        if ser.readline() == b'[\r\n':
            data_array = []
            for i in range(10):
                data_array.append(ser.readline())
            return data_array[2:8]


def decode_data(data_array):
    # Decodifica os bytes em uma string e remove caracteres de espaço em branco e nova linha
    return [item.decode('ASCII').strip() for item in data_array]


def parse_data(data_array):
    return [list(map(float, item.split(','))) for item in data_array]

# Função para inicializar o gráfico de calor


def init_heatmap():
    ax.set_xlim(0, 40)  # Define os limites do eixo x de 0 a 7
    ax.set_ylim(0, 40)  # Define os limites do eixo y de 0 a 7

    cax = plt.imshow(heat_matrix,
                     cmap='coolwarm',
                     interpolation='nearest',
                     vmin=10, vmax=40)  # Ajuste os valores mínimos e máximos conforme necessário
    plt.colorbar(cax)
    return cax

# Função para atualizar o gráfico de calor


def update_heatmap(frame, cax, ser):
    # Atualize a matriz de dados com os novos dados da porta serial
    data = load_data(ser)
    data = decode_data(data)
    data = parse_data(data)
    # Rotaciona e Atualiza a matriz de dados existente
    heat_matrix = np.matrix(data)

    # Atualize o gráfico de calor
    cax.set_data(heat_matrix)
    plt.title('Gráfico de Calor em Tempo Real')


if __name__ == '__main__':
    ser = False
    com_port = 'COM9'
    baud_rate = 115200
    try:
        # OBTENDO DADOS
        # Abre a porta COM

        ser = serial.Serial(com_port, baud_rate)
        # recebe 10 byte objects da porta COM
        data = load_data(ser)
        # decodifica os byte objects em strings
        data = decode_data(data)
        # converte as strings em arrays com números float formando uma matriz 8x8
        data = parse_data(data)

        # PLOTAGEM
        # cria uma matriz no formato do numpy (otimizada)
        heat_matrix = np.matrix(data)

        # Display the received data
        fig, ax = plt.subplots()

        # Inicializa o gráfico de calor
        cax = init_heatmap()

        # Configuração da animação
        ani = FuncAnimation(fig, update_heatmap, fargs=(
            cax, ser), interval=10, cache_frame_data=False)  # Atualiza a cada 10 ms

        plt.show()

    except serial.SerialException as e:
        print(f"Erro: {e}")
        print('exeception')
    finally:
        if ser:
            ser.close()  # Fecha a porta COM quando terminar
            print('desligando')
