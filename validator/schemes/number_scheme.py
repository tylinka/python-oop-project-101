class NumberScheme:
    def __init__(self):
        self._range = ()
        self._required = False
        self._positive = False

    def required(self):
        self._required = True
        return self

    def range(self, a, b):
        self._range = (a, b)
        return self

    def positive(self):
        self._positive = not self._positive
        return self

    def is_valid(self, number):
        if self._required:
            if number is None:
                return False
        if self._positive and number is not None and number <= 0:
            return False
        if len(self._range) > 0 and not self._range[0] <= number <= self._range[1]:
            return False
        return True
