import sqlite3

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