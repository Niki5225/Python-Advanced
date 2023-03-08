from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        elif price > self.__budget:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([x.salary for x in self.workers])
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        care = sum([x.money_for_care for x in self.animals])
        if care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [repr(x) for x in self.animals if isinstance(x, Lion)]
        result += f"----- {len(lions)} Lions:\n" + "\n".join(lions) + "\n"
        tigers = [repr(x) for x in self.animals if isinstance(x, Tiger)]
        result += f"----- {len(tigers)} Tigers:\n" + "\n".join(tigers) + "\n"
        cheetahs = [repr(x) for x in self.animals if isinstance(x, Cheetah)]
        result += f"----- {len(tigers)} Cheetahs:\n" + "\n".join(cheetahs)
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [repr(x) for x in self.workers if isinstance(x, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n" + "\n".join(keepers)  + "\n"
        caretakers = [repr(x) for x in self.workers if isinstance(x, Caretaker)]
        result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(caretakers) + "\n"
        vets = [repr(x) for x in self.workers if isinstance(x, Vet)]
        result += f"----- {len(vets)} Vets:\n" + "\n".join(vets)
        return result
