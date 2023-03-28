class Controller:
    VALID_SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def __get_error_message(player_one, player_two):
        error_message = ''
        if player_one.stamina == 0:
            error_message += f"Player {player_one.name} does not have enough stamina."
        if player_two.stamina == 0:
            error_message += "\n" + f"Player {player_two.name} does not have enough stamina."

        return error_message

    def __find_needed_supply(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[idx].__class__.__name__ == sustenance_type:
                return idx

    def __find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __validate_player_if_in_list(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return True
        else:
            return False

    def __validate_if_drinks(self):
        for supply in self.supplies:
            if supply.__class__.__name__ == "Drink":
                return True
        else:
            return False

    def __validate_if_food(self):
        for supply in self.supplies:
            if supply.__class__.__name__ == "Food":
                return True
        else:
            return False

    def add_player(self, *players):
        added_player_names = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_player_names.append(player.name)
        return f"Successfully added: {', '.join(x for x in added_player_names)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if not self.__validate_player_if_in_list(player_name):
            return
        elif sustenance_type not in self.VALID_SUSTENANCE_TYPES:
            return
        elif sustenance_type == "Drink" and not self.__validate_if_drinks():
            raise Exception("There are no drink supplies left!")
        elif sustenance_type == "Food" and not self.__validate_if_food():
            raise Exception("There are no food supplies left!")
        player = self.__find_player(player_name)
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        idx_supply = self.__find_needed_supply(sustenance_type)
        supply = self.supplies[idx_supply]
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += supply.energy
        self.supplies.pop(idx_supply)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = self.__find_player(first_player_name)
        player_two = self.__find_player(second_player_name)

        error_message = self.__get_error_message(player_one, player_two)

        if error_message:
            return error_message.strip()

        if player_two.stamina < player_one.stamina:
            player_one, player_two = player_two, player_one

        player_one_attack = player_one.stamina / 2
        player_two.stamina = max(0, player_two.stamina - player_one_attack)
        if player_two.stamina == 0:
            return f"Winner: {player_one.name}"

        player_two_attack = player_two.stamina / 2
        player_one.stamina = max(0, player_one.stamina - player_two_attack)
        if player_one.stamina == 0:
            return f"Winner: {player_two.name}"

        if player_one.stamina > player_two.stamina:
            return f"Winner: {player_one.name}"
        else:
            return f"Winner: {player_two.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(0, player.stamina - player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = '\n'.join([str(x) for x in self.players]) + '\n' + \
                 '\n'.join([x.details() for x in self.supplies])

        return result
