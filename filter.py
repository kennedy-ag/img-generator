import numpy as np

class FilterApplier:
    @staticmethod
    def reset_channel(img: np.ndarray, channel: int):
        """
        Sets all the 'channel' of the image 'img' to 0

            Parameters:
                img (ndarray(x, y, 3)): the image-like array\n
                channel (int): channel to be reseted\n
                    0 = 'R'gb\n
                    1 = r'G'b\n
                    2 = rg'B'
        """
        for line in img: 
            for pixel in line: pixel[channel] = 0
    
    @staticmethod
    def fill_channel(img: np.ndarray, channel: int, value=100):
        """
        Fill all the 'channel' of the image 'img' with the 'value'

            Parameters:
                img (ndarray(x, y, 3)): the image-like array\n
                channel (int): channel to be reseted\n
                value (int): the value between 0 and 255 to be set\n
                    0 = 'R'gb\n
                    1 = r'G'b\n
                    2 = rg'B'
        """
        for line in img: 
            for pixel in line: pixel[channel] = value