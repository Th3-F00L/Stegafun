from pixel_enum import Pixel

class Decode:
    @staticmethod
    def sequential(hexcode, pixel_choice): # Determines which hexidecimal RGB value for a given pixel ends with a 0 or 1
        match pixel_choice:
            case Pixel.BLUE:
                if hexcode[-1] in ('0', '1'):
                    return hexcode[-1]
                else:
                    return None
            case Pixel.GREEN:
                if hexcode[-3] in ('0', '1'):
                    return hexcode[-3]
                else:
                    return None
            case Pixel.RED:
                if hexcode[-5] in ('0', '1'):
                    return hexcode[-5]
                else:
                    return None
