import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import pandas as pd

# Carga las coordenadas de las comarcas desde un archivo CSV
comarcas_df = pd.read_csv('comarcas.csv')

# Configura la ventana principal
root = tk.Tk()
root.title("Juego de Adivinar Comarcas de Galicia")

# Carga la imagen y la usa como fondo
path_to_image = 'comarcas1.gif'  # Asegúrate de que la ruta es correcta
img = Image.open(path_to_image)
bg_image = ImageTk.PhotoImage(img)
canvas = tk.Canvas(root, width=img.width, height=img.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=bg_image)

# Función para escribir el nombre de la comarca en la ubicación correcta
def write_comarca(comarca_name):
    # Busca las coordenadas de la comarca en el DataFrame
    comarca_data = comarcas_df[comarcas_df['Nombre'].str.lower() == comarca_name.lower()]
    if not comarca_data.empty:
        # Obtén las coordenadas X y Y
        x, y = comarca_data.iloc[0]['X'], comarca_data.iloc[0]['Y']
        # Crea texto en el canvas en la posición X, Y
        canvas.create_text(x, y, text=comarca_name, fill="black", font=("Arial", 12))


# Inicia el juego
def start_game():
    while True:
        # Pide al jugador que introduzca el nombre de la comarca
        comarca_name = simpledialog.askstring("Adivina la Comarca", "Introduce el nombre de la comarca:")
        if comarca_name in (None, ''):
            break  # Salir del bucle si la entrada es None o vacía
        elif comarca_name.lower() == 'salir':
            break  # Salir del bucle si la entrada es 'salir'
        write_comarca(comarca_name)

    # Cerrar la ventana principal cuando se sale del juego
    root.destroy()


# Ejecuta la función start_game cuando se inicia el programa
root.after(1000, start_game)  # Espera 1 segundo antes de iniciar el juego

root.mainloop()
