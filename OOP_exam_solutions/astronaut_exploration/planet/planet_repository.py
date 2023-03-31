from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        for p in self.planets:
            if p.name == planet.name:
                self.planets.remove(p)
                break

    def find_by_name(self, name: str):
        for planet in self.planets:
            if planet.name == name:
                return planet