from matplotlib import pyplot as plt
import numpy as np

X = 25
Y = 20

def generate_channel_list(x:int, y:int) -> list:
    return np.random.randint(low=0, high=255, size=y*x)

rgb = [generate_channel_list(X, Y) for i in range(3)]
img = np.concatenate((rgb[0], rgb[1], rgb[2])).reshape(Y, X, 3)

plt.imshow(img)