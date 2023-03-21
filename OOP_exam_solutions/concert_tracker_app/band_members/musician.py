from abc import ABC, abstractmethod


class Musician(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    @abstractmethod
    def possible_skills(self):
        pass

    @abstractmethod
    def learn_new_skill(self, new_skill):
        if new_skill not in self.possible_skills():
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for el in value:
            if el.isalpha():
                break
        else:
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value
