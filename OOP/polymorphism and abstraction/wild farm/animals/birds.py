from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_foods(self):
        return ["Meat"]

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def weight_incremental(self):
        return 0.25


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_foods(self):
        return ["Meat", "Seed", "Fruit", "Vegetable"]

    def make_sound(self):
        return "Cluck"

    @property
    def weight_incremental(self):
        return 0.35
