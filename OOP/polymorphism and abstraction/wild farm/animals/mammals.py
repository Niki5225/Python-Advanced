from project.animals.animal import Mammal


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ["Meat"]

    def make_sound(self):
        return "Woof!"

    @property
    def weight_incremental(self):
        return 0.4


class Mouse(Mammal):
    @property
    def allowed_foods(self):
        return ["Vegetable", "Fruit"]

    def make_sound(self):
        return "Squeak"

    @property
    def weight_incremental(self):
        return 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ["Vegetable", "Meat"]

    def make_sound(self):
        return "Meow"

    @property
    def weight_incremental(self):
        return 0.3


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ["Meat"]

    def make_sound(self):
        return "ROAR!!!"

    @property
    def weight_incremental(self):
        return 1

