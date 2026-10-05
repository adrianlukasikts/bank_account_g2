from main import add
import sqlite3

class TestDataBase:
    con = sqlite3.connect("bank.db")
    def test_add_user(self):
        add(self.con, "users", name="1", surname="2", email="cvl", phone="cvl cvl cvl")
