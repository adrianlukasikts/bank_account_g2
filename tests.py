from unittest import TestCase

from functions import add, select
import sqlite3

class TestDataBase(TestCase):
    con = sqlite3.connect("bank.db")
    def test_add_user(self):
        email = "test@email.com"
        add(self.con, table_name="users", name="1", surname="2", email=email, phone="123123123")
        uuid = self.con.cursor().execute("""SELECT id
                                       FROM users
                                       WHERE email = ?""", [email]).fetchmany()
        self.assertTrue(len(uuid)>0)
        result = select(self.con, table_name="users", name="1", surname="2", email=email, phone="123123123")
        print(result)