from datetime import date, timedelta
from library.borrow_record import BorrowRecord

def test_borrow_record_overdue():
    overdue = BorrowRecord(
        book_id = 1,
        user_id = 1,
        due_date = date.today() - timedelta(days=1)
    )

    assert overdue.is_overdue() is True

def test_borrow_record_not_overdue():
    overdue = BorrowRecord(
        book_id = 1,
        user_id = 1,
        due_date = date.today() + timedelta(days=1)
    )

    assert overdue.is_overdue() is False


