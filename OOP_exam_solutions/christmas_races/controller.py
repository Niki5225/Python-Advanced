from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = ["SportsCar", "MuscleCar"]

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def __find_winners(race):
        winners = []
        sorted_by_speed = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]

        for winner in sorted_by_speed:
            winners.append(f"Driver {winner.name} wins the {race.name} race with a speed of {winner.car.speed_limit}.")
            winner.number_of_wins += 1

        return winners

    def __validate_if_all_cars_of_that_type_are_taken_or_not_exist(self, car_type):
        for car in self.cars:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return False
        else:
            return True

    def __find_car(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car

    def __validate_if_car_type_exists(self, car_type):
        for car in self.cars:
            if car.__class__.__name__ == car_type:
                return True
        else:
            return False

    def __validate_car_if_in_list(self, model):
        for car in self.cars:
            if car.model == model:
                return True
        else:
            return False

    def __validate_if_driver_in_list(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return True
        else:
            return False

    def __validate_race_if_in_list(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return True
        else:
            return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CAR_TYPES:
            return
        elif self.__validate_car_if_in_list(model):
            raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            self.cars.append(MuscleCar(model, speed_limit))
        elif car_type == "SportsCar":
            self.cars.append(SportsCar(model, speed_limit))

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__validate_if_driver_in_list(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__validate_race_if_in_list(race_name):
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.__validate_if_driver_in_list(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")
        if self.__validate_if_all_cars_of_that_type_are_taken_or_not_exist(car_type):
            raise Exception(f"Car {car_type} could not be found!")

        new_car = self.__find_car(car_type)
        driver = [d for d in self.drivers if d.name == driver_name][0]
        new_car.is_taken = True

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = new_car
            return f"Driver {driver.name} changed his car from {old_car.model} to {new_car.model}."

        driver.car = new_car
        return f"Driver {driver.name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.__validate_race_if_in_list(race_name):
            raise Exception(f"Race {race_name} could not be found!")
        if not self.__validate_if_driver_in_list(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if driver_name == d.name][0]
        race = [r for r in self.races if r.name == race_name][0]

        if not driver.car:
            raise Exception(f"Driver {driver.name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver.name} is already added in {race.name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.__validate_race_if_in_list(race_name):
            raise Exception(f"Race {race_name} could not be found!")

        race = [r for r in self.races if r.name == race_name][0]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")

        winners = self.__find_winners(race)

        return '\n'.join(winners)
