from convert import Convert

import base64
import cv2

import tkinter as tk
import PIL as pillow
from enum import Enum
from enum import auto
from tkinter import filedialog
from pathlib import Path
from PIL import Image

class Pixel(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()



def encode_message(msg: str):
    root = tk.Tk()
    root.withdraw()

    file_types = [('PNGs', '*.png')]
    img_path = filedialog.askopenfilename(title='Please Select an Image to Hide Your Message In',
                                          initialdir=Path.home() / 'Pictures',
                                          filetypes=file_types)
    img_extension = '.' + img_path.split('.')[-1]

    if img_path:
        # img_binary = ''
        # img = Image.open(img_path)
        # if img.mode in ('RGBA'):
        #     img = img.convert('RGBA')
        #     pixels = img.getdata()
        #     for pixel in pixels:
        #          digit =

        string = Convert.binary_to_string()
        print(string)


        # Write the result to a file
    #     if os.path.exists(secret_img_path):
    #         with open(secret_img_path, 'w') as result:
    #             pass
    #     else:
    #         with open(secret_img_path, 'x') as result:
    #             pass
    #
    # print("Success!")



            # orig_img_bin = base64_to_binstr(orig_img_base64)
            # show_image(img_path)
    else:
        raise FileNotFoundError("Please provide an image file to hide your message in.")


def base64_to_binstr(orig_img_base64):
    return "".join(["{:08b}".format(x) for x in base64.decodebytes(orig_img_base64)])


# def show_image(img_path):
#     img = cv2.imread(img_path)
#     cv2.imshow('image', img)
#     cv2.waitKey()


# encode_message('test')
binary = (Convert.string_to_binary("Hello World!"))
print(binary)
print(Convert.binary_to_string(binary))
