from random import randint
from matplotlib import pyplot as plt
import numpy as np

def generate_channel_list(y_size:int, x_size:int) -> list:
    values_list = []
    resolution = y_size * x_size
    for i in range(resolution):
        values_list.append(randint(0, 255))
    return values_list

X = 22
Y = 20
CHANNELS = 3

reds = generate_channel_list(Y, X)
greens = generate_channel_list(Y, X)
blues = generate_channel_list(Y, X)

lista_full = []
lista_full.extend(reds)
lista_full.extend(greens)
lista_full.extend(blues)

img = np.array(lista_full).reshape(Y, X, CHANNELS)
plt.imshow(img)
