import sqlite3

def connect():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Conexión exitosa")
    return conn, cursor

def insert_user(name, email, password):
    conn, cursor = connect()
    cursor.execute(f'''
        INSERT INTO users(name, email, password)
        VALUES('{name}', '{email}', '{password}')
    ''')
    conn.commit()
    conn.close()
