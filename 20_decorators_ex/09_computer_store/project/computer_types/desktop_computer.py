from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    MAX_RAM = 128

    def configure_computer(self, processor: str, ram: int):
        return self._configure(processor, ram, self.PROCESSORS, self.MAX_RAM, "desktop computer")
