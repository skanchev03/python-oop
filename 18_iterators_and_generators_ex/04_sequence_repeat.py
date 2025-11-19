class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.sequence_len = len(sequence)
        self.sequence_counter = -1
        self.number_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.number_counter < self.number:
            self.sequence_counter += 1
            self.number_counter += 1
            if self.sequence_counter < len(self.sequence):
                return self.sequence[self.sequence_counter]
            else:
                self.sequence_counter = 0
                return self.sequence[self.sequence_counter]
        raise StopIteration()
