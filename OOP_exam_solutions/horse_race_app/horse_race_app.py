from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __find_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        else:
            raise Exception(f"Race {race_type} could not be found!")

    def __find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        else:
            raise Exception(f"Jockey {jockey_name} could not be found!")

    def __find_horse(self, horse_type):
        for horse in self.horses[::-1]:
            if not horse.is_taken and horse.__class__.__name__ == horse_type:
                return horse
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

    def __validate_horse_if_in_list(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

    def __validate_jockey_if_in_list(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        self.__validate_horse_if_in_list(horse_name)
        if horse_type == "Appaloosa":
            self.horses.append(Appaloosa(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."
        elif horse_type == "Thoroughbred":
            self.horses.append(Thoroughbred(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        self.__validate_jockey_if_in_list(jockey_name)
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = HorseRace(race_type)
        for r in self.horse_races:
            if r.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey(jockey_name)
        horse = self.__find_horse(horse_type)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        else:
            jockey.horse = horse
            horse.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race(race_type)
        jockey = self.__find_jockey(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        else:
            race.jockeys.append(jockey)
            return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race(race_type)
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = self.__find_winner(race)
        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def __find_winner(self, race):
        winner = race.jockeys[0]
        for jockey in race.jockeys:
            if jockey.horse.speed > winner.horse.speed:
                winner = jockey
        return winner