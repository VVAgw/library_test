from dataclasses import dataclass
from typing import List
from library.borrow_record import BorrowRecord

@dataclass
class User:
    id: int
    name: str
    borrowed_books: List[BorrowRecord] = []
