class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3, 4, 5, "top")

    def test_init_method(self):
        result = [1, 2, 3, 4, 5]
        self.assertEqual(result, self.list.get_data())

    def test_add_operation(self):
        self.list.add(6)
        result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, self.list.get_data())

    def test_add_error(self):
        with self.assertRaises(ValueError) as context:
            self.list.add(4.4)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_method(self):
        result = self.list.remove_index(0)
        self.assertEqual(1, result)
        self.assertEqual([2, 3, 4, 5], self.list.get_data())

    def test_remove_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.remove_index(77)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_method(self):
        result = 3
        self.assertEqual(result, self.list.get(2))
        self.assertEqual([1, 2, 3, 4, 5], self.list.get_data())

    def test_get_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.get(5555)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_method(self):
        self.list.insert(0, 0)
        self.assertEqual(0, self.list.get_data()[0])
        self.assertEqual([0, 1, 2, 3, 4, 5], self.list.get_data())

    def test_insert_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.insert(4444, 1)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.list.insert(0, "Not_an_integer")

        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest_method(self):
        self.assertEqual(5, self.list.get_biggest())

    def test_get_index_method(self):
        self.assertEqual(0, self.list.get_index(1))


if __name__ == "__main__":
    unittest.main()
