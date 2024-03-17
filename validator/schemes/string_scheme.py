class StringScheme:
    def __init__(self):
        self._min_length = None
        self._required = False
        self._contains = None

    def required(self):
        self._required = True
        return self

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
