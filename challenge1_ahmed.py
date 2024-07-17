import unittest

class Book:
    """
    class book made to represent books with a title, author, and publication year.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.

    """
    def __init__(self, title: str, author :str , year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Returns a string representation of the book.

        Returns:
            str: A string describing the book.
        """
        return f"Book title: '{self.title}' written by {self.author}, in year: {self.year}"

class Library:
    """ class library made to represent a library containing a list/collection of books.

    Attributes:
        books (list): A list of books in the library.
    """
    def __init__(self : list):
        self.books = []

    def add_book(self, book):
        """Add a book to the library.

        Args:
            book (Book): The book to add to the library.
        """
        self.books.append(book)

    def display_books(self):
        """Displays all books in the library."""
        
        result = "List of Books Saved:\n"
        for book in self.books:
            result += str(book) + "\n"
        return result.strip()

    def find_books_by_title(self, title):
        """finds the books in the library that matchs the given title.

        Args:
            title (str): The title of the book to search for.

        Returns:
            list: A list of books that match the title.
        """
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        return found_books

class TestBook(unittest.TestCase):

    def setUp(self):
        book = Book("text correction", "Abdelaal, A", 2024)
        self.assertEqual(book.title, "text correction")
        self.assertEqual(book.author, "Abdelaal, A")
        self.assertEqual(book.year, 2024)

    def test_book_str(self):
        book = Book("text correction", "Abdelaal, A", 2024)
        self.assertEqual(str(book), "Book title: 'text correction' written by Abdelaal, A, in year: 2024")

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book("text correction", "Abdelaal, A", 2024)
        self.book2 = Book("math", "Ahmad", 2020)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        book = Book("math", "Ahmad", 2020)
        self.library.add_book(book)
        self.assertIn(book, self.library.books)

    def test_display_books(self):

        expected_output = """List of Books Saved:
Book title: 'text correction' written by Abdelaal, A, in year: 2024
Book title: 'math' written by Ahmad, in year: 2020"""
        self.assertEqual(self.library.display_books(), expected_output)

    def test_find_books_by_title(self):
        found_books = self.library.find_books_by_title("math")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, "math")

        found_books = self.library.find_books_by_title("science")
        self.assertEqual(len(found_books), 0)


if __name__ == "__main__":
    unittest.main()
