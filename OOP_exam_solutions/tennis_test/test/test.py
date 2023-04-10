from project.tennis_player import TennisPlayer
import unittest


class TennisPlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Gosho", 18, 66)

    def test_init(self):
        self.assertEqual(self.player.name, "Gosho")
        self.assertEqual(self.player.age, 18)
        self.assertEqual(self.player.points, 66)
        self.assertEqual(self.player.wins, [])

    def test_validations_init(self):
        with self.assertRaises(ValueError) as context:
            self.player.name = ""

        self.assertEqual(str(context.exception), "Name should be more than 2 symbols!")

        with self.assertRaises(ValueError) as context:
            self.player.name = "GG"

        self.assertEqual(str(context.exception), "Name should be more than 2 symbols!")

        with self.assertRaises(ValueError) as context:
            self.player.age = 5

        self.assertEqual(str(context.exception), "Players must be at least 18 years of age!")

    def test_win_method(self):
        self.player.add_new_win("Wimbeldon")
        self.assertEqual(self.player.wins, ["Wimbeldon"])
        self.assertEqual(self.player.add_new_win("Wimbeldon"), "Wimbeldon has been already added to the list of wins!")

    def test_lt_method(self):
        player2 = TennisPlayer("Pesho", 18, 67)
        self.assertEqual('Pesho is a top seeded player and he/she is better than Gosho', self.player.__lt__(player2))
        player2.points = 33
        self.assertEqual('Gosho is a better player than Pesho', self.player.__lt__(player2))

    def test_str_method(self):
        self.assertEqual("Tennis Player: Gosho\n"
                         "Age: 18\n"
                         "Points: 66.0\n"
                         "Tournaments won: ", self.player.__str__())

        self.player.add_new_win("Shelf")
        self.player.add_new_win("Iron")

        self.assertEqual("Tennis Player: Gosho\n"
                         "Age: 18\n"
                         "Points: 66.0\n"
                         "Tournaments won: Shelf, Iron", self.player.__str__())


if __name__ == '__main__':
    unittest.main()
