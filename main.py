from convert import Convert
from encode import Encode
from pixel_enum import Pixel
import base64
import os

import tkinter as tk
import PIL as pillow
from PIL import Image
from enum import Enum
from enum import auto
from tkinter import filedialog
from pathlib import Path






def hide_message(msg: str):
    pixel_choice = Pixel.BLUE
    root = tk.Tk()
    root.withdraw()

    file_types = [('PNGs', '*.png')]
    img_path = filedialog.askopenfilename(title='Please Select an Image to Hide Your Message In',
                                          initialdir=Path.home() / 'Pictures',
                                          filetypes=file_types)
    img_extension = '.' + img_path.split('.')[-1]

    if img_path:
        img = Image.open(img_path)
        delimiter = ('1'*15)+'0'
        msg_binary = Convert.string_to_binary(msg) + delimiter
        print(msg_binary)

        if img.mode in ('RGBA'):
            img = img.convert('RGBA')
            pixels = img.getdata()
            new_pixels = []
            msg_binary_index = 0
            temp = ''
            for pixel in pixels:
                if msg_binary_index < len(msg_binary):
                    new_pixel = Encode.sequential(Convert.rgb_to_hex(pixel[0], pixel[1], pixel[2]),
                                                  msg_binary[msg_binary_index], pixel_choice)
                    if new_pixel == None
                        new_pixels.append(pixel)
                    else:
                        r, g, b = Convert.hex_to_rgb(new_pixel)
                        new_pixels.append((r, g, b, 255))
                        msg_binary_index += 1
                else: new_pixels.append(pixel)
            secret_img_path = f"{img_path.strip(img_extension)}_secret{img_extension}"
            result_img = Image.new("RGBA", img.size)
            result_img.putdata(new_pixels)
            result_img.save(secret_img_path, "PNG")
            return f"Operation completed. Secret image saved at {secret_img_path}"

       return "Image uses an incompatible image mode. Please choose another image."



def base64_to_binstr(orig_img_base64):
    return "".join(["{:08b}".format(x) for x in base64.decodebytes(orig_img_base64)])


# def show_image(img_path):
#     img = cv2.imread(img_path)
#     cv2.imshow('image', img)
#     cv2.waitKey()


hide_message('Hello World!')
