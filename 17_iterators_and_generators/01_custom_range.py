class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start - 1   # so the first next() returns start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        raise StopIteration
