import numpy as np
from PIL import Image


def ft_load(path: str):
    image = Image.open(path)
    image = image.convert("RGB")
    print(f"The shape of image is: {np.array(image).shape}")
    return  np.array(image)