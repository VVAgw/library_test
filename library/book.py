from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    autor: str
    # добавить флаг доступности
