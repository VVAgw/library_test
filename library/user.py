from dataclasses import dataclass
from typing import List

@dataclass
class User:
    id: int
    name: str
    borrowed_books: List[BorrowRecord] = []

    def borrow_book(self, record: BorrowRecod):
        raise NotImplementedError("тут должен быть метод")

    def return_book(book_id: int):
        raise NotImplementedError("тут должен быть метод")
