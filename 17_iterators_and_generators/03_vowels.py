class vowels:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            if char in "aeiouAEIOUyY":
                return char
        raise StopIteration
