from sqlite3 import Connection, Cursor



def add(con: Connection, table_name: str, **params) -> None:
    con.cursor().execute(f"INSERT INTO {table_name}({', '.join(params.keys())}) VALUES ({', '.join(['?'] * len(params))});",
                list(params.values()))
    con.commit()

def select(con: Connection, table_name: str, **params) -> Cursor:
    result = con.cursor().execute(f"SELECT * FROM {table_name} WHERE {' AND '.join([f'{k} = ?' for k in params])};",
                list(params.values()))
    return result

def add_user(con: Connection, name: str, surname: str, email: str, phone: str, login: str, password: str):
    class UserAlreadyExists(Exception):
        ...

    cursor = con.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION;")
        add(con, table_name="users", name=name, surname=surname, email=email, phone=phone)
        user_id = select(con, table_name="users", email=email).fetchone()[0]
        add(con, table_name="credentials", login=login, password=password, user_id=user_id)
        cursor.execute("COMMIT;")
    except UserAlreadyExists:
        cursor.execute("ROLLBACK;")









