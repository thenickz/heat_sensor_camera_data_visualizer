import serial
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# color map reference: https://matplotlib.org/stable/gallery/color/colormap_reference.html
# Função para gerar uma matriz 8x8 aleatória


def generate_random_data():
    return np.random.rand(8, 8)

# Função para inicializar o gráfico de calor


def init_heatmap():
    data = np.zeros((8, 8))
    cax = plt.imshow(data, cmap='rainbow',
                     interpolation='nearest', vmin=0, vmax=1)
    plt.colorbar(cax)
    return cax

# Função para atualizar o gráfico de calor


def update_heatmap(frame, cax):
    data = generate_random_data()
    cax.set_data(data)
    plt.title('Gráfico de Calor em Tempo Real')


# Define the COM port and baud rate
# Change this to your COM port (e.g., COM1, COM2, COM3, etc.)
com_port = 'COM9'
baud_rate = 9600  # Use the same baud rate as configured in your ESP32 code

try:
    # Open the COM port
    ser = serial.Serial(com_port, baud_rate)

    print(f"Reading data from {com_port}...")

    while True:
        # Read data from the COM port (you can specify the number of bytes to read)
        data = ser.readline()  # Reads a line of text (assuming your ESP32 sends data as text)

        # Display the received data
        # Decoding to UTF-8 assuming it's text data
        print(f"Received data: {data}")

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    if ser.is_open:
        ser.close()  # Close the COM port when done


'''# Configuração inicial do gráfico
fig, ax = plt.subplots()

# Inicializa o gráfico de calor
cax = init_heatmap()

# Configuração da animação
ani = FuncAnimation(fig, update_heatmap, fargs=(
    cax,), interval=1000)  # Atualiza a cada 1 segundo

plt.show()'''
