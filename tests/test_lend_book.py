from datetime import date
from library.library import Library
from library.user import User
from library.borrow_record import BorrowRecord
from library.book import Book

def test_lend_book_basic():
    libr = Library("My library")
    book = Book(id=3, autor="WA", title="Test")
    usr = User(user_id=3, user_name="vva")

    libr.register_user(usr)
    libr.add_book(book)

    due = date(2025,10,10)
    libr.lend_book(book_id=3, user_id=3, due_date=due)

    assert book.is_available is False
    assert len(usr.borrowed_books) == 1
    record = usr.borrowed_books[0]
    assert record.book_id == 3
    assert record.user_id == 3
    assert record.due_date == due

    assert book.active_record is record
