from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6
    REFUEL_EFFICIENCY = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER_CONSUMPTION)
        if required_fuel <= self.fuel_quantity:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.REFUEL_EFFICIENCY
