import sqlite3
import uuid

con = sqlite3.connect("bank.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users
               (
                   id      INTEGER PRIMARY KEY AUTOINCREMENT,
                   name    VARCHAR(50) NOT NULL,
                   surname VARCHAR(50) NOT NULL,
                   email   VARCHAR(50) NOT NULL UNIQUE,
                   phone   VARCHAR(12) NOT NULL
               )""")

cur.execute("""CREATE TABLE IF NOT EXISTS accounts
               (
                   id      INTEGER PRIMARY KEY AUTOINCREMENT,
                   amount  DECIMAL(20, 2) NOT NULL,
                   user_id INTEGER        NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id)
               )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS transactions
               (
                   id          INTEGER PRIMARY KEY AUTOINCREMENT,
                   amount      DECIMAL(10, 2) NOT NULL,
                   account_from_id INTEGER        NOT NULL,
                   account_to_id   INTEGER        NOT NULL,
                   date        VARCHAR(20)    NOT NULL,
                   FOREIGN KEY (account_from_id) REFERENCES accounts (id),
                   FOREIGN KEY (account_to_id) REFERENCES accounts (id),
                   CHECK (account_from_id != account_to_id)
               )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS credentials
               (
                   id       INTEGER PRIMARY KEY AUTOINCREMENT,
                   login    VARCHAR(50)  NOT NULL,
                   password VARCHAR(150) NOT NULL,
                   user_id  INTEGER      NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users (id)
               )
            """)

program_is_finished = False



def add_user(name, surname, email, phone, login, password):
    cur.execute("""INSERT INTO users(name, surname, email, phone) VALUES (?, ?, ?, ?)""", (name, surname, email, phone))
    con.commit()
    uuid = cur.execute("""SELECT id FROM users WHERE email = ?""", (email)).fetchone()[0]
    cur.execute("""INSERT INTO credentials(login, password, user_id) VALUES (?, ?, ?)""", (login, password, uuid))
    con.commit()

while not program_is_finished:
    print("1. Log in")
    print("2. Sing up")
    print("3. Exit Program")
    user_input = input("Enter number for program execution: ")
    match user_input:
        case "1":
            ...
        case "2":
            add_user(input("Enter your Name: "), input("Enter your Surname: "), input("Enter your E-Mail: "), input("Enter your Phone Number: "), input("Enter "), input())
        case "3":
            program_is_finished = True
        case _:
            print("Please enter a correct option")













