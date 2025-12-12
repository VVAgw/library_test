

class Book:
    def __init__(self, id: int, title: str, autor: str):
        self.id = id
        self.title = title
        self.autor = autor
        self.is_available = True
        self.active_record = None
