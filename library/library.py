from typing import List
from .book import Book
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
            if user.id == user_id:
                self.users.remove(user)
                break
        #raise NotImplementedError("тут должен быть метод")

    def add_book(self, book: Book) -> None:
        raise NotImplementedError("тут должен быть метод")

    def remove_book(self, book_id: int) -> None:
        raise NotImplementedError("тут должен быть метод")
    
    # функция поиска книги приветная 
    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def lend_book(self, book_id: int, user_id: int, due_date: date):
        rc = BorrowRecor(book_id=book_id, user_id=user_id, due_date=due_date)
        usr = self.users[user_id]
        usr.borrow_book(book)
        book = self.books[book_id]
        book.is_avaliable = False
        book.active_record = rc

    def return_book(self, book_id: int):
        raise NotImplementedError("тут должен быть метод")
