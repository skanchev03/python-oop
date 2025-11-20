from abc import ABC, abstractmethod


class Computer(ABC):
    VALID_RAM_SIZES = [2 ** i for i in range(1, 8)]  # 2 → 128

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value or value.strip() == "":
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value or value.strip() == "":
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    def _configure(self, processor, ram, processors, max_ram, type_name):
        if processor not in processors:
            raise ValueError(f"{processor} is not compatible with {type_name} {self.manufacturer} {self.model}!")
        if ram not in self.VALID_RAM_SIZES or ram > max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {type_name} {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        ram_price = (ram.bit_length() - 1) * 100
        self.price = processors[processor] + ram_price
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
