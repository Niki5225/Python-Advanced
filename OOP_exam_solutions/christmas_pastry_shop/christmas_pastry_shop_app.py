from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        elif type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))
        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))
        else:
            raise Exception(f"{type_booth} is not a valid booth!")

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for b in self.booths:
            if b.capacity >= number_of_people and not b.is_reserved:
                b.reserve(number_of_people)
                return f"Booth {b.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def validate_order(self, booth_number, delicacy_name):
        booth = None
        delicacy = None
        for b in self.booths:
            if b.booth_number == booth_number:
                booth = b
                break
        for d in self.delicacies:
            if d.name == delicacy_name:
                delicacy = d
                break

        return booth, delicacy

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth, delicacy = self.validate_order(booth_number, delicacy_name)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = booth.get_bill()
        self.income += bill
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
