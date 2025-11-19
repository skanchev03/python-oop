class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        while self.index < len(self.dictionary):
            key = list(self.dictionary.keys())[self.index]
            value = self.dictionary[key]
            return (key, value)
        raise StopIteration
