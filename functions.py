from sqlite3 import Connection


def add(con: Connection, table_name: str, **params) -> None:
    con.cursor().execute(f"INSERT INTO {table_name}({', '.join(params.keys())}) VALUES ({', '.join(['?'] * len(params))})",
                list(params.values()))
    con.commit()

def select(con: Connection, table_name: str, **params):
    result = con.cursor().execute(f"SELECT * FROM {table_name} WHERE {' AND '.join([f'{k} = ?' for k in params])}",
                list(params.values()))
    return result


