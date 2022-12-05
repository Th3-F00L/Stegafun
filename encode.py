from pixel_enum import Pixel


class Encode:

    @staticmethod
    def sequential(hexcode, binary_digit, pixel_choice):
        match pixel_choice:
            case Pixel.BLUE:
                if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
                    hexcode = hexcode[:-1] + binary_digit
                    return hexcode
                else:
                    return None
            case Pixel.GREEN:
                if hexcode[-3] in ('0', '1', '2', '3', '4', '5'):
                    saved_bits = hexcode[5:]
                    tampered_bits = hexcode[:-3] + binary_digit
                    hexcode = tampered_bits + saved_bits
                    return hexcode
                else:
                    return None
            case Pixel.RED:
                if hexcode[-5] in ('0', '1', '2', '3', '4', '5'):
                    saved_bits = hexcode[3:]
                    tampered_bits = hexcode[:-5] + binary_digit
                    hexcode = tampered_bits + saved_bits
                    return hexcode
                else:
                    return None

