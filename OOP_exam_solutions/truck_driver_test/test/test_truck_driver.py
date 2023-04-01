from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Gosho", 20)

    def test_init_method(self):
        self.assertEqual("Gosho", self.driver.name)
        self.assertEqual(20, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_validation(self):
        with self.assertRaises(ValueError) as context:
            self.driver.earned_money += -4

        self.assertEqual("Gosho went bankrupt.", str(context.exception))

    def test_add_cargo_method(self):
        self.assertEqual(f"Cargo for 200 to Dubai was added as an offer.", self.driver.add_cargo_offer("Dubai", 200))
        self.assertEqual({"Dubai": 200}, self.driver.available_cargos)
        with self.assertRaises(Exception) as context:
            self.driver.add_cargo_offer("Dubai", 200)
        self.assertEqual("Cargo offer is already added.", str(context.exception))

    def test_driver_best_cargo_offer(self):
        self.assertEqual(self.driver.drive_best_cargo_offer(), "There are no offers available.")
        self.driver.add_cargo_offer("Dubai", 200)
        self.driver.add_cargo_offer("Plovdiv", 600)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.miles, 600)
        self.assertEqual(self.driver.earned_money, 11960)
        self.assertEqual(self.driver.drive_best_cargo_offer(), "Gosho is driving 600 to Plovdiv.")

    def test_check_for_activities(self):
        self.driver.earned_money += 100000
        self.driver.check_for_activities(10000)
        self.assertEqual(self.driver.earned_money, 88250)

    def test_repr_method(self):
        self.assertEqual("Gosho has 0 miles behind his back.", self.driver.__repr__())

if __name__ == "__main__":
    unittest.main()