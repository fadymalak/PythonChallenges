import unittest

from challenge1_amrelkfrawy import Library, Book

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.book = Book("Fluent Python", "Luciano Ramalho", 2015)
        self.lib = Library()
        self.lib.add_book(self.book)
        
    def test_add_book(self):
        self.assertIn(self.book, self.lib.books)
        self.assertEqual(len(self.lib.books), 1)

        lib = Library()
        self.assertEqual(len(lib.books), 0)

    
    def test_display_books(self):
        result = [str(book) for book in self.lib.books]
        self.assertEqual(self.lib.display_books(), result)
    
    def test_find_book_by_title(self):
        self.assertEqual(self.lib.find_book_by_title("Fluent Python"), self.book)
        self.assertEqual(self.lib.find_book_by_title("Fluent Python1"), 'Book not found')

class TestBook(unittest.TestCase):
    def test_str(self):
        book = Book("Fluent Python", "Luciano Ramalho", 2015)
        self.assertEqual(str(book), "Fluent Python - Luciano Ramalho 2015")

if __name__ == "__main__":
    unittest.main()