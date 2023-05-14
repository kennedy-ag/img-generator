from matplotlib import pyplot as plt
import numpy as np
import time

class Image:

    @staticmethod
    def __generate_channel_list(x:int, y:int) -> list:
        return np.random.randint(low=0, high=255, size=y*x)
    
    @staticmethod
    def generate_image(x: int, y: int) -> np.ndarray:
        rgb = [Image.__generate_channel_list(x, y) for i in range(3)]
        img = np.concatenate((rgb[0], rgb[1], rgb[2])).reshape(x, y, 3)
        return img
    
    @staticmethod
    def save(img: np.ndarray):
        plt.savefig(f"images/{int(time.mktime(time.localtime()))}.png")

    @staticmethod
    def show(img: np.ndarray):
        plt.imshow(img)