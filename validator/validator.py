from validator.schemes import StringScheme, NumberScheme, ListScheme, DictScheme


class Validator:
    def __init__(self):
        self.custom_validations = {
            'string': {},
            'number': {},
            'list': {},
            'dict': {},
        }

    def string(self):
        return StringScheme(self.custom_validations['string'])

    def number(self):
        return NumberScheme(self.custom_validations['number'])

    def list(self):
        return ListScheme(self.custom_validations['list'])

    def dict(self):
        return DictScheme(self.custom_validations['dict'])

    def add_validator(self, val_type, val_name, fn):
        self.custom_validations[val_type][val_name] = {
            'function': fn, 'value': None
        }
