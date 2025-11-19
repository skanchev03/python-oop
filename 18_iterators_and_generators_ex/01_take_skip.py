class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.count <= 0:
            raise StopIteration

        self.count -= 1
        return self.step * self.number
