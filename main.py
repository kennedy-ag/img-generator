from filter import FilterApplier
from image import Image
import numpy as np

img = Image.generate_image(720, 1080)
FilterApplier.reset_channel(img, 1)
FilterApplier.fill_channel(img, 2, 10)

Image.save(img)