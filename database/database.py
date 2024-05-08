import sqlite3

def connect():

    # Conexión a la base de datos (creará un archivo de base de datos llamado 'biblioteca.db' si no existe)
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    try:
    # Creación de la tabla 'usuarios'
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (

                            nombre TEXT PRIMARY KEY,
                            email TEXT,
                            password TEXT,
                            fecha_registro TEXT DEFAULT (DATETIME('now')),
                            administrador INTEGER NULL DEFAULT 0
                        )''')

        # Creación de la tabla 'libros'
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
                            id INTEGER PRIMARY KEY,
                            titulo TEXT,
                            autor TEXT,
                            fecha_publicacion TEXT,
                            genero TEXT,
                            disponible INTEGER
                        )''')

        # Creación de la tabla 'libros_prestados'
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros_prestados (
                            id INTEGER PRIMARY KEY,
                            id_libro INTEGER,
                            id_usuario INTEGER,
                            fecha_prestamo TEXT,
                            fecha_devolucion TEXT,
                            devuelto INTEGER
                        )''')
    except sqlite3.Error as e:
        print("Error al crear las tablas: ", e)

    # Guardar cambios y cerrar la conexión
    conn.commit()
    conn.close()
    print("Conexión exitosa")
    return conn, cursor


def close(conn):
    conn.close()
    print("Conexión cerrada")


def insert_user(conn, cursor, nombre, email, password):
    
    try:
        cursor.execute('''INSERT INTO usuarios (nombre, email, password)
                        VALUES (?, ?, ?)''', (nombre, email, password))
        conn.commit()
        print("Usuario registrado")
    except sqlite3.Error as e:
        print("Error al registrar usuario: ", e)

def login_user(conn, cursor, nombre, password):
    try:
        cursor.execute('''SELECT * FROM usuarios WHERE nombre = ? AND password = ?''', (nombre, password))
        user = cursor.fetchone()
        if user:
            print("Inicio de sesión exitoso")
            return True
        else:
            print("Credenciales incorrectas")
            return False
    except sqlite3.Error as e:
        print("Error al iniciar sesión: ", e)
        return False