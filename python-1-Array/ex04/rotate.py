from PIL import Image
from load_image import ft_load
import os

def main():
    print(ft_load("animal.jpeg"))
    with Image.open("animal.jpeg") as im:
        cuted = im.crop((im.width / 4 , im.height / 4 , 4 * im.width /  4  , 4 * im.height/ 4))
        cuted.rotate(90).show()
        cuted.save("res.jpeg")
        ft_load('res.jpeg')
        os.remove('res.jpeg')



if __name__ == "__main__":
    main()