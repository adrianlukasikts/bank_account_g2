from sqlite3 import Connection, Cursor
from typing import Any


class ElementAlreadyExists(Exception):
    ...


class UserNotExist(Exception):
    ...

def add(con: Connection, table_name: str, **params) -> None:
    con.cursor().execute(
        f"INSERT INTO {table_name}({', '.join(params.keys())}) VALUES ({', '.join(['?'] * len(params))});",
        list(params.values()))
    con.commit()


def select(con: Connection, table_name: str, **params) -> list[Any]:
    cursor = con.cursor().execute(f"SELECT * FROM {table_name} WHERE {' AND '.join([f'{k} = ?' for k in params])};",
                                  list(params.values()))
    result = cursor.fetchmany()
    if not result:
        raise UserNotExist()

    return result

def try_add(con: Connection, table_name: str, **params) -> None:
    result = select(con, table_name, **params)
    if result:
        raise ElementAlreadyExists()
    add(con, table_name, **params)



def add_user(con: Connection, name: str, surname: str, email: str, phone: str, login: str, password: str):
    cursor = con.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION;")
        try_add(con, table_name="users", name=name, surname=surname, email=email, phone=phone)
        user_id = select(con, table_name="users", email=email)[0][0]
        add(con, table_name="credentials", login=login, password=password, user_id=user_id)
        cursor.execute("COMMIT;")
    except ElementAlreadyExists:
        cursor.execute("ROLLBACK;")
        print("ten użytkownik już istnieje")
    except UserNotExist:
        cursor.execute("ROLLBACK;")
        print("nie znaleziono użytkownika")

