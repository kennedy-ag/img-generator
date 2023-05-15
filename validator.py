import numpy as np

class Validator:
    
    @staticmethod
    def validate_image(img: np.ndarray):
        if img.shape[0] < 1 or img.shape[1] < 1:
            raise ValueError("The dimensions of image must be greater than 0.")
        if img.shape[2] < 3 or img.shape[2] > 4:
            raise ValueError("The number of channels of image must be 3 or 4.")
    
    @staticmethod
    def validate_channel(channel: int):
        if channel < 0 or channel > 2:
            raise ValueError("The number of the channel must be 0, 1 or 2.")
        
    @staticmethod
    def validate_value_of_fill(value: int):
        if value < 0 or value > 255:
            raise ValueError("The value to fill the channel with must be between 0 and 255.")