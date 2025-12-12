from typing import List
from library.borrow_record import BorrowRecord

class User:
    def __init__(self, user_id: int, user_name: str): 
        self.user_id = user_id
        self.user_name = user_name
        self.borrowed_books: List[BorrowRecord] = []

    def borrow_book(self, record: BorrowRecord):
        self.borrowed_books.append(record) 
