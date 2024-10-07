import sqlite3

def connection_db():
    return sqlite3.connect('crud.db')

if __name__ == "__main__":
    connection_db()