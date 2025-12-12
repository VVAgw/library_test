from dataclasses import dataclass
from typing import List
from library.borrow_record import BorrowRecord

@dataclass
class User:
    id: int
    name: str
    borrowed_books: List[BorrowRecord] = []

    def borrow_book(self. record: BorrowRecord):
        self.borrowed_books.append(record) 
