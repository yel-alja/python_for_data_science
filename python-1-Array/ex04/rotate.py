from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt
import os

def main():
    print(ft_load("animal.jpeg"))
    with Image.open("animal.jpeg") as im:
        cuted = im.crop((im.width / 4 , im.height / 4 , 4 * im.width /  4  , 4 * im.height/ 4))
        cuted = cuted.rotate(90).convert("L")
        plt.imshow(cuted, cmap="gray")
        plt.show()



if __name__ == "__main__":
    main()