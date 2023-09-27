from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import serial


def parse(data):
    # Decodifica os bytes em uma string e remove caracteres de espaço em branco e nova linha
    data_str = data.decode('utf-8').strip()

    # Divide a string em valores separados por vírgula e transforma cada valor em float
    return list(map(float, data_str.split(',')))


def init_heatmap():
    # Função para inicializar o gráfico de calor
    data = np.zeros((8, 8))
    cax = plt.imshow(data, cmap='rainbow',
                     interpolation='nearest', vmin=0, vmax=1)
    plt.colorbar(cax)
    return cax


def update_heatmap(frame, cax):
    # Lê novos dados do sensor da câmera via porta serial
    read_data = ser.readline()
    for i in range(10):
        # Read data from the COM port (you can specify the number of bytes to read)
        # Reads a line of text (assuming your ESP32 sends data as text)

        if 9 > i > 0:
            cax[i, :] = parse(read_data)
        elif i == 0:
            continue
        elif i == 9:
            break

        # Converte os dados em uma lista de números
        new_data = parse(read_data)

    # Atualiza a matriz de dados do gráfico de calor
    cax.set_data(np.array(new_data).reshape(8, 8))

    # Define os limites do gráfico de calor, se necessário
    cax.set_clim(vmin=0, vmax=1)

    plt.title('Gráfico de Calor em Tempo Real')


com_port = 'COM9'
baud_rate = 9600

# Display the received data
fig, ax = plt.subplots()

# Inicializa o gráfico de calor
cax = init_heatmap()

try:
    # Open the COM port
    ser = serial.Serial(com_port, baud_rate)

    # Configuração da animação
    ani = FuncAnimation(fig, update_heatmap, fargs=(
        cax,), interval=10)  # Atualiza a cada 10 milissegundos
    plt.show()

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    if ser.is_open:
        ser.close()  # Close the COM port when done
