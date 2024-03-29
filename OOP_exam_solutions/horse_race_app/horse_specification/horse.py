from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @abstractmethod
    def train(self):
        pass

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value
