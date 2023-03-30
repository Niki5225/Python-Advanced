class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Ivan", 444, 0)

    def test_init_method(self):
        self.assertEqual(self.worker.name, "Ivan")
        self.assertEqual(self.worker.salary, 444)
        self.assertEqual(self.worker.energy, 0)

    def test_energy_after_rest_method(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 1)

    def test_for_energy_is_zero_or_negative(self):
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_worker_salary(self):
        self.worker.rest()
        self.worker.work()
        self.assertEqual(self.worker.money, 444)

    def test_worker_energy(self):
        self.worker.rest()
        self.worker.work()
        self.assertEqual(self.worker.energy, 0)

    def test_method_get_info(self):
        result = self.worker.get_info()
        self.assertEqual(result, f'Ivan has saved 0 money.')


if __name__ == "__main__":
    unittest.main()
