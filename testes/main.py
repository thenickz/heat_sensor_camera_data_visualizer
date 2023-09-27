from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import serial


def parse(data):
    # 1 - corta string entre indices 2 e 56,
    # 2 - entre cada virgula transforma o valor em float
    # 3 - retorna uma lista
    return list(map(float, data[2:56].slit(',')))


def init_heatmap():
    # Função para inicializar o gráfico de calor
    data = np.zeros((8, 8))
    cax = plt.imshow(data, cmap='rainbow',
                     interpolation='nearest', vmin=0, vmax=1)
    plt.colorbar(cax)
    return cax


def update_heatmap(frame, cax):
    data = 1
    cax.set_data(data)
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
    for i in range(10):
        # Read data from the COM port (you can specify the number of bytes to read)
        # Reads a line of text (assuming your ESP32 sends data as text)
        read_data = ser.readline()
        if 9 > i > 0:
            cax[i, :] = parse(read_data)
        elif i == 0:
            continue
        elif i == 9:
            break

    # Configuração da animação
    ani = FuncAnimation(fig, update_heatmap, fargs=(
        cax,), interval=10)  # Atualiza a cada 1 segundo
    plt.show()

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    if ser.is_open:
        ser.close()  # Close the COM port when done
