from validator.schemes.number_scheme import NumberScheme
from validator.schemes.string_scheme import StringScheme


class Validator:
    def __init__(self):
        pass

    @staticmethod
    def string():
        return StringScheme()

    @staticmethod
    def number():
        return NumberScheme()
