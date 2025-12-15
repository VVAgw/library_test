from datetime import date
from library.borrow_record import BorrowRecord
from library.user import User
from library.book import Book
from library.library import Library

def test_return_book_bosic():
    libr = Library("MyLibr")
    user = User(user_id=3, user_name="WA")
    book = Book(id=4, title="World?", autor="Psh")
    libr.add_book(book)
    libr.register_user(user)

    due = date(2025, 1, 1)
    libr.lend_book(book_id=4, user_id=3, due_date=due)

    libr.return_book(book_id=4)

    assert book.is_available is True
    assert book.active_record is None
    assert len(user.arrwed_books) == 0
