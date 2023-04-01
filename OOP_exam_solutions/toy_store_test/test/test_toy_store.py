from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_init_method(self):
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None})

    def test_add_toy_method(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("N", "Hoe")

        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

        self.assertEqual(self.toy_store.add_toy("A", "Hoe"), "Toy:Hoe placed successfully!")

        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("A", "Hoe")
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

        with self.assertRaises(Exception) as context:
            self.toy_store.add_toy("A", "Truck")
        self.assertEqual("Shelf is already taken!", str(context.exception))

        self.assertEqual("Toy:Ninja placed successfully!", self.toy_store.add_toy("B", "Ninja"))

    def test_remove_method(self):
        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy("M", "E")

        self.assertEqual("Shelf doesn't exist!", str(context.exception))

        with self.assertRaises(Exception) as context:
            self.toy_store.remove_toy("C", "EE")

        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")

        self.toy_store.add_toy("C", "Ninja")
        self.assertEqual("Remove toy:Ninja successfully!", self.toy_store.remove_toy("C", "Ninja"))
        self.assertEqual(None, self.toy_store.toy_shelf["C"])


if __name__ == "__main__":
    unittest.main()
