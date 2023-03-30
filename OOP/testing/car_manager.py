class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class TestGunitSquad(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "M8", 30, 200)

    def test_init_method(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M8", self.car.model)
        self.assertEqual(30, self.car.fuel_consumption)
        self.assertEqual(200, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ''

        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_model_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ''
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -6

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0

        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_validation(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -67

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0

        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1

        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_method(self):
        self.car.refuel(122)
        self.assertEqual(122, self.car.fuel_amount)

        self.car.refuel(100)
        self.assertEqual(200, self.car.fuel_amount)

    def test_refuel_error(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-111)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.refuel(0)

        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_method(self):
        self.car.refuel(100)
        self.car.drive(100)
        self.assertEqual(70, self.car.fuel_amount)

    def test_drive_error(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(111)

        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == "__main__":
    unittest.main()
