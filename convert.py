import binascii

class Convert:

    @staticmethod
    def string_to_binary(string: str) -> str:
        bin_array = [bin(ord(x))[2:].zfill(8) for x in string]
        bin_str = ""
        i = 0
        while i < len(bin_array):
            bin_str += bin_array[int(i)]
            i += 1
        return bin_str

    @staticmethod
    def binary_to_string(bin_str: str) -> str:
        raw_str = binascii.unhexlify('%x' % (int('0b'+bin_str, 2)))
        display_str = (str(raw_str).lstrip('b').replace("'", "").strip('"'))
        return display_str

    @staticmethod
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r,g,b)

    @staticmethod
    def hex_to_rgb(hexcode: str):
        hexcode = hexcode.lstrip('#')
        rgb_values = tuple(int(hexcode[i:i+2], 16) for i in (0,2,4))
        return rgb_values[0], rgb_values[1], rgb_values[2]
