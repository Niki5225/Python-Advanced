class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Fluffy")

    def test_size_incrementation(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_if_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed, True)

    def test_if_error_is_raised_when_trying_to_eat_while_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertEqual(str(context.exception), 'Already fed.')

    def test_error_when_trying_to_sleep_hungry(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()

        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')

    def test_if_cat_is_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()
