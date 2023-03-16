from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type, name, age):
        musicians = ["Guitarist", "Drummer", "Singer"]

        if musician_type not in musicians:
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{musician.name} is already a musician!")

        if musician_type == "Guitarist":
            self.musicians.append(Guitarist(name, age))
        elif musician_type == "Drummer":
            self.musicians.append((Drummer(name, age)))
        else:
            self.musicians.append((Singer(name, age)))
        return f"{name} is now a {musician_type}."

    def create_band(self, name):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            # TODO check the type of the genre
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        for musician in self.musicians:
            if musician.name == musician_name:
                searched_musician = musician
                break
        else:
            raise Exception(f"{musician_name} isn't a musician!")

        for band in self.bands:
            if band.name == band_name:
                band.members.append(searched_musician)
                return f"{musician_name} was added to {band_name}."
        else:
            raise Exception(f"{band_name} isn't a band!")

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        for band in self.bands:
            if band.name == band_name:
                current_band = band
                break
        else:
            raise Exception(f"{band_name} isn't a band!")

        for musician in current_band.members:
            if musician.name == musician_name:
                current_musician = musician
                break
        else:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        current_band.members.remove(current_musician)
        return f"{musician_name} was removed from {band_name}."

    def find_genre(self, place):
        for concert in self.concerts:
            if concert.place == place:
                return concert.genre

    def find_concert(self, place):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def find_band(self, name):
        for band in self.bands:
            if band.name == name:
                return band

    def start_concert(self, concert_place: str, band_name: str):
        concert = self.find_concert(concert_place)
        band = self.find_band(band_name)
        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(filter(lambda x: x.__class__.__name__ == musician_type, band.members)):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        if concert.genre == 'Rock':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing high pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play rock" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and \
                        "play the drums with drumsticks" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and "sing low pitch notes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play metal" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' \
                        and "play the drums with drum brushes" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' \
                        and ("sing low pitch notes" not in band_member.skills
                             or "sing high pitch notes" not in band_member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and "play jazz" not in band_member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
    