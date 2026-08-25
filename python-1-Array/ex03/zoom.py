from PIL import Image
from load_image import ft_load
import os

def main():
    print(ft_load("animal.jpeg"))
    with Image.open("animal.jpeg") as im:
        zoomed = im.crop((im.width / 4 , im.height/4 , 3 * im.width / 4 , 3 * im.height/ 4))
        zoomed.show()
        zoomed.save("zoomed.jpeg")
        print(ft_load("zoomed.jpeg"))
        os.remove("zoomed.jpeg")

if __name__ == "__main__":
    main()