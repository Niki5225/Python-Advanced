from project.library import Library
import unittest


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library("Name")

    def test_init_method(self):
        self.assertEqual("Name", self.library.name)
        self.assertEqual({}, self.library.readers)
        self.assertEqual({}, self.library.books_by_authors)

    def test_name_error(self):
        with self.assertRaises(ValueError) as context:
            self.library.name = ""

        self.assertEqual(str(context.exception), "Name cannot be empty string!")

    def test_add_book_method(self):
        self.library.add_book("Az", "Kniga")
        self.assertEqual(self.library.books_by_authors, {"Az": ["Kniga"]})
        self.library.add_book("Az", "Kniga 2")
        self.assertEqual(self.library.books_by_authors, {"Az": ["Kniga", "Kniga 2"]})

    def test_add_reader_method(self):
        self.library.add_reader("George")
        self.assertEqual(self.library.readers, {"George": []})
        self.assertEqual(self.library.add_reader("George"), "George is already registered in the Name library.")

    def test_rent_a_book_method(self):
        self.assertEqual(self.library.rent_book("az", "Az", "Kniga"), "az is not registered in the Name Library.")
        self.library.add_reader("George")
        self.assertEqual(self.library.rent_book("George", "Az", "Kniga"), "Name Library does not have any Az's books.")
        self.library.add_book("Az", "Kniga")
        self.assertEqual(self.library.rent_book("George", "Az", "Kniga1"), 'Name Library does not have Az\'s "Kniga1".')
        self.library.rent_book("George", "Az", "Kniga")
        self.assertEqual(self.library.readers, {"George": [{"Az": "Kniga"}]})
        self.assertEqual(self.library.books_by_authors, {"Az": []})


if __name__ == "__main__":
    unittest.main()
