from typing import List, Union


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"{self.title} - {self.author} {self.year}"


class Library:
    def __init__(self) -> None:
        self.books: List = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def display_books(self) -> List:
        return [str(book) for book in self.books]

    def find_book_by_title(self, title: str) -> Union[Book, str]:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return "Book not found"


if __name__ == "__main__":
    lib = Library()

    lib.add_book(Book("Fluent Python", "Luciano Ramalho", 2015))
    lib.add_book(Book("Grokking Algorithms", " Sander Rossel", 2015))
    lib.add_book(Book("Learn Python the Hard Way", "Zed Shaw", 2013))

    print(lib.display_books())
    print()

    title = input("Enter book title: ")
    book = lib.find_book_by_title(title)
    print(book)
