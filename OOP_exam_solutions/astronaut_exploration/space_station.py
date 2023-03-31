from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = ["Biologist", "Geodesist", "Meteorologist"]

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_successful_missions = 0
        self.number_of_unsuccessful_missions = 0

    def __validate_if_astronaut_name_in_list(self, name):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return True
        else:
            return False

    def __validate_if_planet_name_in_list(self, name):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return True
        else:
            return False

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception(f"Astronaut type is not valid!")
        if self.__validate_if_astronaut_name_in_list(name):
            return f"{name} is already added."

        astronaut = None

        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut = Meteorologist(name)

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.__validate_if_planet_name_in_list(name):
            return f"{name} is already added."

        items = items.split(", ")
        planet = Planet(name)
        planet.items.extend(items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if not self.__validate_if_astronaut_name_in_list(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

        astronaut = self.astronaut_repository.find_by_name(name)
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        sorted_astronauts = sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)
        if sorted_astronauts[0].oxygen <= 30:
            raise Exception("You need at least one astronaut to explore the planet!")

        suitable_astronauts = []
        for astronaut in sorted_astronauts:
            if len(suitable_astronauts) == 5:
                break
            if astronaut.oxygen > 30:
                suitable_astronauts.append(astronaut)
            else:
                break

        for a in suitable_astronauts:
            while planet.items and a.oxygen > 0:
                a.backpack.append(planet.items.pop())
                a.breathe()

        if not planet.items:
            self.number_of_successful_missions += 1
            return f"Planet: {planet_name} was explored. {len([a for a in suitable_astronauts if a.backpack])} astronauts participated in collecting items."

        else:
            self.number_of_unsuccessful_missions += 1
            return "Mission is not completed."

    def report(self):
        result = ''
        result += f"{self.number_of_successful_missions} successful missions!\n"
        result += f"{self.number_of_unsuccessful_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"
        for a in self.astronaut_repository.astronauts:
            result += f"Name: {a.name}\n"
            result += f"Oxygen: {a.oxygen}\n"
            if a.backpack:
                result += f"Backpack items: {', '.join(a.backpack)}\n"
            else:
                result += f"Backpack items: none\n"
        return result.strip()
