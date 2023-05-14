from filter import FilterApplier
from image import Image
import numpy as np
# TODO implementar validações de entrada das funções

img = Image.generate_image(50, 80)
FilterApplier.reset_channel(img, 1)
FilterApplier.fill_channel(img, 1, 30)

Image.show(img)
Image.save(img)