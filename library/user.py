from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    # добавить список выданных книг
