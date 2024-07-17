class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book Title: {self.title} & Book Author: {self.author} & Publish Year: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No Books Found. Library is Empty.")
        else:
            for book in self.books:
                print(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return "Book Not Found!"


import unittest
from io import StringIO
import sys

class TestLib(unittest.TestCase):

    def setUp(self):
        book1 = Book('Atomic Habits', 'James Clear', 2020)
        book2 = Book("Harry Potter: Philosopher's Stone", "J.K. Rowling", 2000)
        self.library = Library()
        self.library.add_book(book1)
        self.library.add_book(book2)

    def test_book_initialization(self):
        book = Book('Atomic Habits', 'James Clear', 2020)
        self.assertEqual(book.title, 'Atomic Habits')
        self.assertEqual(book.author, 'James Clear')
        self.assertEqual(book.year, 2020)

    def test_library_initialization(self):
        self.assertEqual(len(self.library.books), 2)

    def test_library_add_book(self):
        new_book = Book('Deep Work', 'Cal Newport', 2016)
        self.library.add_book(new_book)
        self.assertEqual(len(self.library.books), 3)
        self.assertEqual(self.library.books[-1], new_book)
    
    def test_library_display_books(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.library.display_books()
        
        sys.stdout = sys.__stdout__
        captured_output = captured_output.getvalue()

        self.assertIn("Atomic Habits", captured_output)
        self.assertIn("Harry Potter: Philosopher's Stone", captured_output)

    def test_find_existing_book_by_title(self):
        result = self.library.find_book_by_title('Atomic Habits')
        self.assertIsInstance(result, Book)
        self.assertEqual(result.title, 'Atomic Habits')

    def test_find_nonexistent_book_by_title(self):
        result = self.library.find_book_by_title('Deep Work')
        self.assertEqual(result, "Book Not Found!")

if __name__ == '__main__':
    unittest.main()
