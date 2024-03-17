import abc


class BasicScheme:
    def __init__(self):
        self._required = False

    def required(self):
        self._required = True
        return self

    @abc.abstractmethod
    def is_valid(self, something):
        return


class ListScheme(BasicScheme):
    def __init__(self):
        super().__init__()
        self._sizeof = None

    def sizeof(self, size):
        self._sizeof = size
        return self

    def is_valid(self, sequence):
        if self._required:
            if sequence is None or not isinstance(sequence, list):
                return False
        if self._sizeof is not None:
            if sequence is not None and len(sequence) != self._sizeof:
                return False
        return True


class NumberScheme(BasicScheme):
    def __init__(self):
        super().__init__()
        self._range = ()
        self._positive = False

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


class StringScheme(BasicScheme):
    def __init__(self):
        super().__init__()
        self._min_length = None
        self._contains = None

    def min_len(self, length):
        self._min_length = length
        return self

    def contains(self, substr):
        self._contains = substr
        return self

    def is_valid(self, text):
        if self._required:
            if text is None or len(text) == 0:
                return False
        if self._contains is not None and self._contains not in text:
            return False
        if self._min_length is not None and len(text) < self._min_length:
            return False
        return True
