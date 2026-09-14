import sqlite3

con = sqlite3.connect("library.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users
               (
                   id      INTEGER PRIMARY KEY AUTOINCREMENT,
                   name    VARCHAR(50) NOT NULL,
                   surname VARCHAR(50) NOT NULL,
                   email   VARCHAR(50) NOT NULL UNIQUE,
                   phone   VARCHAR(12) NOT NULL
               )""")

cur.execute("""CREATE TABLE IF NOT EXISTS transactions
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount DECIMAL(10,2) NOT NULL,
                userfrom_id INTEGER NOT NULL,
                userto_id INTEGER NOT NULL,
                date VARCHAR(20) NOT NULL,
                FOREIGN KEY (userfrom_id) REFERENCES users(id),
                FOREIGN KEY (userto_id) REFERENCES users(id),
                CHECK (userfrom_id != userto_id)
               )
                """)
