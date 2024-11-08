"""This is the bookstore exercise, it is pretty easy."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author, price, and rating.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        :param rating: book's rating
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __eq__(self, other):
        """Check if two books are the same based on title and author."""
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __repr__(self):
        """Provide a string representation for debugging."""
        return f"Book(title='{self.title}', author='{self.author}', price={self.price}, rating={self.rating})"


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has a name, a rating threshold, and an inventory of books.

        :param name: book store name
        :param rating: rating threshold for books in the store
        """
        self.name = name
        self.rating = rating
        self.booksinstore = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if a book can be added.

        A book can be added if:
        1. There is no book with the same title and author already in the store.
        2. The book's rating is greater than or equal to the store's rating.

        :param book: The book to check
        :return: True if the book can be added, False otherwise
        """
        if book in self.booksinstore:
            return False

        return book.rating >= self.rating

    def add_book(self, book: Book) -> bool:
        """
        Add a book to the store if it meets the conditions.

        :param book: The book to add
        :return: True if the book was added, False otherwise
        """
        if self.can_add_book(book):
            self.booksinstore.append(book)
            return True
        return False

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if a book can be removed from the store.

        A book can be removed if it is present in the store.

        :param book: The book to check
        :return: True if the book is in the store, False otherwise
        """
        return book in self.booksinstore

    def remove_book(self, book: Book) -> bool:
        """
        Remove a book from the store if possible.

        :param book: The book to remove
        :return: True if the book was removed, False otherwise
        """
        if self.can_remove_book(book):
            self.booksinstore.remove(book)
            return True
        return False

    def get_all_books(self) -> list:
        """
        Return a list of all books in the store.

        :return: list of Book objects
        """
        return self.booksinstore

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest to most expensive).

        :return: list of Book objects
        """
        return sorted(self.booksinstore, key=lambda book: book.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of books with the highest rating.

        :return: list of Book objects with the highest rating
        """
        if not self.booksinstore:
            return []
        highest_rating = max(book.rating for book in self.booksinstore)
        return [book for book in self.booksinstore if book.rating == highest_rating]


store = Store("Book Haven", 4.0)
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99, 4.5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 8.99, 4.8)
book3 = Book("1984", "George Orwell", 7.99, 4.2)

store.add_book(book1)
store.add_book(book2)
store.add_book(book3)

print(store.get_all_books())
print(store.get_books_by_price())
print(store.get_most_popular_book())
