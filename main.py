from filter import FilterApplier
from image import Image
import numpy as np

img = Image.generate_image(70, 130)
FilterApplier.reset_channel(img, 1)
FilterApplier.fill_channel(img, 1, 110)

Image.show(img)
Image.save(img)