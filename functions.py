from sqlite3 import Connection


def add(con: Connection, table_name: str, **params) -> None:
    con.cursor().execute(f"INSERT INTO {table_name}({', '.join(params.keys())}) VALUES ({', '.join(['?'] * len(params))})",
                list(params.values()))
    con.commit()

def select():
    pass