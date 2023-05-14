from matplotlib import pyplot as plt
import numpy as np

X = 40
Y = 30

def generate_channel_list(x:int, y:int) -> list:
    return np.random.randint(low=0, high=255, size=y*x)

def reset_channel(img: np.ndarray, channel: int):
    for line in img: 
        for pixel in line: pixel[channel] = 0
            
def fill_channel(img: np.ndarray, channel: int, value=100):
    for line in img: 
        for pixel in line: pixel[channel] = value

rgb = [generate_channel_list(X, Y) for i in range(3)]
img = np.concatenate((rgb[0], rgb[1], rgb[2])).reshape(Y, X, 3)

reset_channel(img, 2)
fill_channel(img, 1, 40)

plt.imshow(img)