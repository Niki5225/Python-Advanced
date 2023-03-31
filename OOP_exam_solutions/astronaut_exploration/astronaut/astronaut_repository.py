from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        for a in self.astronauts:
            if a.name == astronaut.name:
                self.astronauts.remove(a)
                break

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
