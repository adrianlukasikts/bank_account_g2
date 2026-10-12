from unittest import TestCase

from functions import add
import sqlite3

class TestDataBase(TestCase):
    con = sqlite3.connect("bank.db")
    def test_add_user(self):
        add(self.con, "users", name="1", surname="2", email="cvl", phone="cvl cvl cvl")
