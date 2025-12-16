from datetime import date

class BorrowRecord:
    def __init__(self, book_id: int, user_id: int, due_date: date):
        self.book_id = book_id
        self.user_id = user_id
        self.due_date = due_date

    def is_overdue(self) -> bool:
        return date.today() > self.due_date

    def calculate_fine(self, daily_rate: int) -> int:
        if not self.is_overdue():
            return 0

        days_overdue = (date.today() - self.due_date).days
        return days_overdue * daily_rate
