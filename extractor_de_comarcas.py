from tkinter import simpledialog
import tkinter as tk
from PIL import Image, ImageTk
import csv

# Inicializa una lista global para almacenar los nombres y coordenadas
comarcas = []

def save_to_csv(comarcas_list, filename='comarcas2.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre', 'X', 'Y'])  # Escribe los encabezados de las columnas
        writer.writerows(comarcas_list)

def get_x_and_y(event):
    # Esta función se llama cuando se hace clic en la imagen
    x, y = event.x, event.y
    nombre_comarca = simpledialog.askstring("Input", "Nombre de la comarca:",
                                            parent=root)
    if nombre_comarca:
        print('Comarca:', nombre_comarca, 'X =', x, 'Y =', y)
        comarcas.append((nombre_comarca, x, y))
        save_to_csv(comarcas)

def show_image(path_to_image):
    global root  # La ventana principal debe ser accesible globalmente
    root = tk.Tk()
    img = Image.open(path_to_image)
    tk_img = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=img.width, height=img.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=tk_img)
    canvas.bind("<Button-1>", get_x_and_y)
    root.mainloop()


show_image(r'C:\Users\34692\PycharmProjects\CSV\juego de comarcas\comarcas1.png')
