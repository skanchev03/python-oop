from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    MAX_RAM = 64

    def configure_computer(self, processor: str, ram: int):
        return self._configure(processor, ram, self.PROCESSORS, self.MAX_RAM, "laptop")
