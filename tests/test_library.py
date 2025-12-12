from library.book import Book
from library.user import User
from library.library import Library

def test_register_user_basic():
    libr = Library("Моя библиотека")
    usr = User(user_id=1, user_name="Джони")
    libr.register_user(usr)
    assert usr in libr.users

def test_remove_user_basic():
    libr = Library("Моя библиотека")
    usr1 = User(user_id=2, user_name="Dog")
    usr2 = User(user_id=3, user_name="Jack")
    libr.register_user(usr1)
    libr.register_user(usr2)
    libr.remove_user(2)
    assert usr1 not in libr.users
    assert usr2 in libr.users
