from PIL import Image

# Abre la imagen original
original_img = Image.open(r'C:\Users\34692\PycharmProjects\CSV\juego de comarcas\comarcas2.gif')

# Define las nuevas dimensiones
nuevo_ancho = 1000
nuevo_alto = 936

# Cambia el tamaño de la imagen
resized_img = original_img.resize((nuevo_ancho, nuevo_alto))

# Guarda la imagen redimensionada
resized_img.save(r'C:\Users\34692\PycharmProjects\CSV\juego de comarcas\comarcas2.gif')
