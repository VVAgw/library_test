from typing import List
from .book import Book
from .user import User

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.users: List[User] = []

    def register_user(self, user: User) -> None:
        raise NotImplementedError("тут должен быть метод")

    def remove_user(self, user_id: int) -> None:
        raise NotImplementedError("тут должен быть метод")

    def add_book(self, book: Book) -> None:
        raise NotImplementedError("тут должен быть метод")

    def remove_book(self, book_id: int) -> None:
        raise NotImplementedError("тут должен быть метод")
