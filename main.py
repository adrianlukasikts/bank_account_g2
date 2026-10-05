import sqlite3
from sqlite3 import Connection



def add(con: Connection, table_name: str, **params) -> None:
    con.cursor().execute(f"INSERT INTO {table_name}({', '.join(params.keys())}) VALUES ({', '.join(['?'] * len(params))})",
                list(params.values()))
    con.commit()

program_is_finished = False

con = sqlite3.connect("bank.db")

while not program_is_finished:
    print("1. Log in")
    print("2. Sing up")
    print("3. Exit Program")
    user_input = input("Enter number for program execution: ")
    match user_input:
        case "1":
            ...
        case "2":
            name, surname, email, phone, login, password = input("Enter your Name: "), input(
                "Enter your Surname: "), input("Enter your E-Mail: "), input("Enter your Phone Number: "), input(
                "enter your login"), input("enter your password")
            add(table_name="users", name=name, surname=surname, email=email, phone=phone)
            uuid = con.cursor().execute("""SELECT id
                                  FROM users
                                  WHERE email = ?""", [email]).fetchone()[0]
            add("credentials", login=login, password=password, user_id=uuid)
        case "3":
            program_is_finished = True
        case _:
            print("Please enter a correct option")
