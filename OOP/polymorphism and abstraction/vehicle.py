from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CONDITIONER = 0.9

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel


class Truck(Vehicle):
    AIR_CONDITIONER = 1.6

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONER)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

