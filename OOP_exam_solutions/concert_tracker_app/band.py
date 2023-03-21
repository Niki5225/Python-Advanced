class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for el in value:
            if el.isalpha():
                break
        else:
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

