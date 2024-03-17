from validator.schemes import StringScheme, NumberScheme, ListScheme


class Validator:
    @staticmethod
    def string():
        return StringScheme()

    @staticmethod
    def number():
        return NumberScheme()

    @staticmethod
    def list():
        return ListScheme()
