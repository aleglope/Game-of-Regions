from PIL import Image

# Abre la imagen original
img = Image.open(r'C:\Users\34692\PycharmProjects\CSV\juego de comarcas\comarcas2.png')

# Convierte la imagen a formato GIF
img = img.convert('RGB')
img.save(r'C:\Users\34692\PycharmProjects\CSV\juego de comarcas\comarcas2.gif')
