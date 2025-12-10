from datetime import date

class BorrowRecord:
    def __init__(self, book_id: int, user_id: int, due_date: date):
        self.book_id = book_id
        self.user_id = user_id
        self.due_date = due_date
