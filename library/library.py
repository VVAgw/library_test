from datetime import date
from typing import List
from .book import Book
from .borrow_record import BorrowRecord
from .user import User

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.users: List[User] = []

    def register_user(self, user: User) -> None:
        self.users.append(user)
        #raise NotImplementedError("тут должен быть метод")

    def remove_user(self, user_id: int) -> None:
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                break
        #raise NotImplementedError("тут должен быть метод")

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book_id: int) -> None:
        raise NotImplementedError("тут должен быть метод")
    
    # функция поиска книги - приватная 
    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    # функция поиска пользователя - приватная
    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    # выдача книги
    def lend_book(self, book_id: int, user_id: int, due_date: date):
        book = self.find_book(book_id)
        if not book:
            print(f"Указанной книги не существует!")
            return

        user = self.find_user(user_id)
        if not user:
            print(f'Указанного пользователя не существует!')
            return

        if book.is_available:
            record = BorrowRecord(book_id=book_id, user_id=user_id, due_date=due_date)
        else:
            print(f'Указанная книга занята!')
            return
        
        user.borrow_book(record)
        book.is_available = False
        book.active_record = record
    
    def return_book(self, book_id: int):
        raise NotImplementedError("тут должен быть метод")
