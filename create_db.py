import sqlite3

def create_db():
    with open('tables.sql', 'r', encoding='utf-8') as f:
        sql = f.read()

    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(sql)


if __name__ == '__main__':
    create_db()