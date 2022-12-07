from enum import Enum
from enum import auto


class RGB(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


class EncodingMode(Enum):
    SIMPLE = auto()
    FIZZBUZZ = auto()


class EncryptionOptions(Enum):
    NONE = auto()
    AES = auto()
    ARIA = auto()
    RC6 = auto()
    SERPENT = auto()
    SM4 = auto()
    TWOFISH = auto()


class Operation(Enum):
    CONCEAL = 0
    RECOVER = 1


