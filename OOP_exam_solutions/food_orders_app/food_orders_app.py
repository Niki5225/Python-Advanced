from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __find_client(self, client_phone_number):
        for c in self.clients_list:
            if c.phone_number == client_phone_number:
                return c

    def __check_if_client_is_registered(self, client_phone_number):
        for c in self.clients_list:
            if c.phone_number == client_phone_number:
                return True
        else:
            return False

    def register_client(self, client_phone_number: str):
        result = self.__check_if_client_is_registered(client_phone_number)
        if result:
            raise Exception("The client has already been registered!")
        else:
            self.clients_list.append(Client(client_phone_number))
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Starter) or isinstance(meal, MainDish) or isinstance(meal, Dessert):
                self.menu.append(meal)

    def show_menu(self):
        self.__validate_menu()
        result = ''
        for meal in self.menu:
            result += meal.details() + "\n"
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__validate_menu()
        if not self.__check_if_client_is_registered(client_phone_number):
            self.register_client(client_phone_number)
        client = self.__find_client(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if meal_name not in client.current_order:
                client.current_order[meal_name] = 0
            client.current_order[meal_name] += meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.current_order.items():
            for meal in self.menu:
                if ordered_meal == meal.name:
                    meal.quantity += quantity

        client.bill = 0
        client.shopping_cart = []
        client.current_order = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount" \
               f" of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} " \
               f"meals on the menu and {len(self.clients_list)} clients."
