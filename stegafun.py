from convert import Convert
from encode import Encode
from decode import Decode
from enums import RGB
from PIL import Image


def conceal_msg(msg: str, img_path, rgb_choice):

    img_extension = '.' + img_path.split('.')[-1]
    delimiter = ('1' * 15) + '0'
    if img_path:
        img = Image.open(img_path)
        msg_binary = Convert.string_to_binary(msg) + delimiter

        if img.mode in 'RGBA':
            img = img.convert('RGBA')
            pixels = img.getdata()
            new_pixels = []
            msg_binary_index = 0
            for pixel in pixels:
                if msg_binary_index < len(msg_binary):
                    new_pixel = Encode.sequential(Convert.rgb_to_hex(pixel[0], pixel[1], pixel[2]),
                                                  msg_binary[msg_binary_index], rgb_choice)
                    if new_pixel == None:
                        new_pixels.append(pixel)
                    else:
                        r, g, b = Convert.hex_to_rgb(new_pixel)
                        new_pixels.append((r, g, b, 255))
                        msg_binary_index += 1
                else:
                    new_pixels.append(pixel)
            secret_img_path = f"{img_path.strip(img_extension)}_secret{img_extension}"
            result_img = Image.new("RGBA", img.size)
            result_img.putdata(new_pixels)
            result_img.save(secret_img_path, "PNG")
            return f"Operation completed. Secret image saved at {secret_img_path}"
        return "Image uses an incompatible image mode. Please choose another image."


def recover_msg(img_path, rgb_choice: RGB):
    file_types = [('PNGs', '*.png')]
    img = Image.open(img_path)
    binary_msg = ''
    delimiter = ('1' * 15) + '0'

    if img.mode in 'RGBA':
        img = img.convert('RGBA')
        pixels = img.getdata()
        for pixel in pixels:
            binary_digit = Decode.sequential(Convert.rgb_to_hex(pixel[0], pixel[1], pixel[2]), rgb_choice)
            if binary_digit is None:
                pass
            else:
                binary_msg = binary_msg + binary_digit
                if binary_msg[-16:] == delimiter:
                    print("Operation Completed Successfully")
                    return Convert.binary_to_string(binary_msg[:-16])
    return "Image uses an incompatible image mode. Could not retrieve message."
