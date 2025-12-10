from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    autor: str
    is_avaliable: bool
