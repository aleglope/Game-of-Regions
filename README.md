🌍🎮 Guess the Regions of Galicia Game 🕹️

## Descripción.📜 

Este proyecto es un juego interactivo en el que los jugadores deben adivinar las comarcas de Galicia en un mapa. El juego está desarrollado utilizando Python y la biblioteca Tkinter para la interfaz gráfica de usuario.

## Requerimientos.📋

Antes de ejecutar el juego, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x 🐍
- Tkinter 🖼️
- Pillow 🖼️
- Pandas 🐼

Puedes instalar las dependencias necesarias utilizando pip:

```sh
pip install tkinter pillow pandas
```

## Archivos necesarios.📁

Para que el juego funcione correctamente, necesitarás los siguientes archivos:

1. `main.py`: El archivo principal del juego.
2. `comarcas.csv`: Archivo CSV que contiene los nombres y coordenadas de las comarcas.
3. `comarcas1.gif`: Imagen del mapa de Galicia en formato GIF.
4. `comarcas2.png` y `comarcas2.gif`: Imágenes utilizadas para la conversión y redimensionamiento.

## Instrucciones de uso.🛠️

### Paso 1: Configuración del entorno

1. Asegúrate de que todos los archivos necesarios estén en el mismo directorio.
2. Verifica que las rutas a las imágenes y al archivo CSV en el código sean correctas.

### Paso 2: Preparación del archivo CSV

Para preparar el archivo CSV `comarcas.csv`, sigue estos pasos:

1. Ejecuta el script para asignar coordenadas a las comarcas:

```python
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import csv

comarcas = []

def save_to_csv(comarcas_list, filename='comarcas2.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Nombre', 'X', 'Y'])  # Escribe los encabezados de las columnas
        writer.writerows(comarcas_list)

def get_x_and_y(event):
    x, y = event.x, event.y
    nombre_comarca = simpledialog.askstring("Input", "Nombre de la comarca:", parent=root)
    if nombre_comarca:
        print('Comarca:', nombre_comarca, 'X =', x, 'Y =', y)
        comarcas.append((nombre_comarca, x, y))
        save_to_csv(comarcas)

def show_image(path_to_image):
    global root
    root = tk.Tk()
    img = Image.open(path_to_image)
    tk_img = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(root, width=img.width, height=img.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=tk_img)
    canvas.bind("<Button-1>", get_x_and_y)
    root.mainloop()

show_image('path_to_your_image.png')
```

2. Reemplaza `'path_to_your_image.png'` con la ruta a tu imagen de comarcas y ejecuta el script. Esto permitirá que asignes coordenadas a las comarcas haciendo clic en el mapa y guardando los datos en `comarcas2.csv`.

### Paso 3: Conversión y redimensionamiento de imágenes

Si necesitas convertir o redimensionar la imagen del mapa, usa los siguientes scripts:

- Para convertir una imagen a formato GIF:

```python
from PIL import Image

img = Image.open('path_to_your_image.png')
img = img.convert('RGB')
img.save('path_to_your_image.gif')
```

- Para redimensionar una imagen:

```python
from PIL import Image

original_img = Image.open('path_to_your_image.gif')
nuevo_ancho = 1000
nuevo_alto = 936
resized_img = original_img.resize((nuevo_ancho, nuevo_alto))
resized_img.save('path_to_your_image.gif')
```

### Paso 4: Ejecutar el juego

Una vez que todo esté configurado, puedes ejecutar el juego utilizando el archivo `main.py`:

```python
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
path_to_image = 'comarcas1.gif'
img = Image.open(path_to_image)
bg_image = ImageTk.PhotoImage(img)
canvas = tk.Canvas(root, width=img.width, height=img.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor="nw", image=bg_image)

def write_comarca(comarca_name):
    comarca_data = comarcas_df[comarcas_df['Nombre'].str.lower() == comarca_name.lower()]
    if not comarca_data.empty:
        x, y = comarca_data.iloc[0]['X'], comarca_data.iloc[0]['Y']
        canvas.create_text(x, y, text=comarca_name, fill="black", font=("Arial", 12))

def start_game():
    while True:
        comarca_name = simpledialog.askstring("Adivina la Comarca", "Introduce el nombre de la comarca:")
        if comarca_name in (None, ''):
            break
        elif comarca_name.lower() == 'salir':
            break
        write_comarca(comarca_name)
    root.destroy()

root.after(1000, start_game)
root.mainloop()
```


## Contribuciones🤝

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit de los mismos (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.
