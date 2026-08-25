from PIL import Image
import numpy as np 
def ft_invert(array):
    """Inverts the color of the image received."""
    Image.fromarray(array).show()
    arr = 255 - array
    Image.fromarray(arr).show()


def ft_red(array):
    """red effect"""
    arr = array.copy()
    arr[: ,: , 1] = 0
    arr[: ,: , 2] = 0
    Image.fromarray(arr).show()
    
def ft_green(array):
    """green effect"""
    arr = array.copy()
    arr[: ,: , 0] = 0
    arr[: ,: , 2] = 0
    Image.fromarray(arr).show()

def ft_blue(array):
    """blue effect"""
    arr = array.copy()
    arr[: ,: , 0] = 0
    arr[: ,: , 1] = 0
    Image.fromarray(arr).show()

def ft_grey(array):
    """grey effect"""
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    Image.fromarray(grey_image.astype(np.uint8)).show()
    print(grey_image.ndim)