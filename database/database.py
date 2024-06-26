import sqlite3

def connect():
    try:
        # Conexión a la base de datos (creará un archivo de base de datos llamado 'biblioteca.db' si no existe)
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        # Creación de la tabla 'usuarios'
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            nombre TEXT PRIMARY KEY,
                            email TEXT,
                            password TEXT,
                            fecha_registro TEXT DEFAULT (DATETIME('now')),
                            administrador INTEGER NULL DEFAULT 0
                        )''')
        cursor.execute('''INSERT OR IGNORE INTO usuarios (nombre, email, password, administrador)
                        VALUES ('admin', 'admin', 'admin', 1), ('user', 'user', 'user', 0), ('user2', 'user2', 'user2', 0)''')

        # Creación de la tabla 'libros'
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros (
                            id INTEGER PRIMARY KEY,
                            titulo TEXT,
                            autor TEXT,
                            fecha_publicacion TEXT,
                            genero TEXT,
                            disponible INTEGER,
                            portada TEXT
                        )''')

        libros = [
            (1, 'El señor de los anillos', 'J.R.R. Tolkien', '1954-07-29', 'Fantasía', 1, './src/bookscover/elseñor.jpg'),
            (2, 'Cien años de soledad', 'Gabriel García Márquez', '1967-05-30', 'Realismo mágico', 1, './src/bookscover/cienaños.png'),
            (3, '1984', 'George Orwell', '1949-06-08', 'Distopía', 1, './src/bookscover/1984.jpg'),
            (4, 'Orgullo y prejuicio', 'Jane Austen', '1813-01-28', 'Romance', 1, './src/bookscover/orgullo.jpg'),
            (5, 'Don Quijote de la Mancha', 'Miguel de Cervantes', '1605-01-01', 'Novela de caballería', 1, './src/bookscover/donquijote.jpg'),
            (6, 'Harry Potter y la piedra filosofal', 'J.K. Rowling', '1997-06-26', 'Fantasía', 1, './src/bookscover/lapiedra.jpg'),
            (7, 'Matar a un ruiseñor', 'Harper Lee', '1960-07-11', 'Ficción legal', 1, './src/bookscover/matar.jpg'),
            (8, 'Crónica de una muerte anunciada', 'Gabriel García Márquez', '1981-05-05', 'Realismo mágico', 1, './src/bookscover/cronica.jpg'),
            (9, 'La metamorfosis', 'Franz Kafka', '1915-10-15', 'Ficción filosófica', 1, './src/bookscover/metamorfosis.jpg'),
            (10, 'Las aventuras de Tom Sawyer', 'Mark Twain', '1876-12-10', 'Novela de aventuras', 1, './src/bookscover/aventuras.jpg'),
            (11, 'Hamlet', 'William Shakespeare', '1603-01-01', 'Tragedia', 1, './src/bookscover/hamlet.jpg'),
            (12, 'Drácula', 'Bram Stoker', '1897-05-26', 'Novela gótica', 1, './src/bookscover/dracula.jpg'),
            (13, 'Frankenstein', 'Mary Shelley', '1818-01-01', 'Ciencia ficción', 1, './src/bookscover/frankestein.jpg'),
            (14, 'La odisea', 'Homero', '1200-01-01', 'Epopeya', 1, './src/bookscover/odisea.jpg'),
            (15, 'La iliada', 'Homero', '1800-01-01', 'Epopeya', 1, './src/bookscover/iliada.jpg'),
            (16, 'Moby Dick', 'Herman Melville', '1851-11-14', 'Novela de aventuras', 1, './src/bookscover/mobydick.jpg'),
            (17, 'El gran Gatsby', 'F. Scott Fitzgerald', '1925-04-10', 'Ficción psicológica', 1, './src/bookscover/gran.jpg'),
            (18, 'Los miserables', 'Victor Hugo', '1862-04-03', 'Novela histórica', 1, './src/bookscover/miserables.jpg'),
            (19, 'Anna Karenina', 'León Tolstói', '1877-01-01', 'Novela psicológica', 1, './src/bookscover/anna.jpg'),
            (20, 'El retrato de Dorian Gray', 'Oscar Wilde', '1890-07-01', 'Ficción gótica', 1, './src/bookscover/retrato.jpg')
        ]

        # Inserción de datos en la tabla 'libros'
        cursor.executemany('''INSERT OR IGNORE INTO libros (id, titulo, autor, fecha_publicacion, genero, disponible, portada)
                              VALUES (?, ?, ?, ?, ?, ?, ?)''', libros)

        # Creación de la tabla 'libros_prestados'
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros_reservados (
                            id_reserva INTEGER PRIMARY KEY,
                            id_libro INTEGER,
                            usuario TEXT,
                            fecha_prestamo TEXT,
                            fecha_devolucion TEXT,
                            devuelto INTEGER
                        )''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios_bloqueados (
                            
                            nombre TEXT PRIMARY KEY
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS proximos_libros (
                            titulo TEXT PRIMARY KEY,
                            autor TEXT,
                            fecha_publicacion TEXT,
                            genero TEXT,
                            portada TEXT
                        )''')
                       
        libros_proximos = [
            ('El principito', 'Antoine de Saint-Exupéry', '1943-04-06', 'Literatura infantil', './src/bookscover/principito.jpg'),
            ('El alquimista', 'Paulo Coelho', '1988-01-01', 'Novela de aventuras', './src/bookscover/alquimista.jpg'),
            ('El amor en los tiempos del cólera', 'Gabriel García Márquez', '1985-01-01', 'Realismo mágico', './src/bookscover/amor.jpg'),
            ('La sombra del viento', 'Carlos Ruiz Zafón', '2001-01-01', 'Novela de misterio', './src/bookscover/sombra.jpg'),
            ('Rayuela', 'Julio Cortázar', '1963-01-01', 'Ficción experimental', './src/bookscover/rayuela.jpg')
        ]
        cursor.executemany('''INSERT OR IGNORE INTO proximos_libros (titulo, autor, fecha_publicacion, genero, portada)
                      VALUES (?, ?, ?, ?, ?)''', libros_proximos)

        # Guardar cambios y cerrar la conexión
        conn.commit()
        conn.close()
        print("Conexión exitosa")
        return conn, cursor

    except sqlite3.Error as e:
        print("Error al conectar o al crear las tablas: ", e)


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
    cursor.execute('''
        SELECT * 
        FROM usuarios 
        WHERE nombre = ? AND password = ?
    ''', (nombre, password))
    
    user = cursor.fetchone()
    
    if user:
        nombre = user[0]
        cursor.execute('''
            SELECT 1 
            FROM usuarios_bloqueados 
            WHERE nombre = ?
        ''', (nombre,))
        
        blocked = cursor.fetchone()
        
        if blocked:
            print("Usuario bloqueado")
            return False
        else:
            print("Inicio de sesión exitoso")
            return True
    else:
        print("Credenciales incorrectas")
        return False


    
def title_to_id(conn, cursor, title):
    cursor.execute('SELECT id FROM libros WHERE titulo = ?', (title,))
    result = cursor.fetchone()
    if result:
        print(f"El id del libro '{title}' es {result[0]}.")
        return result[0]
    else:
        print(f"No se encontró ningún libro con el título '{title}'.")
        return None
    

def obtener_info_libro_por_id(id_libro):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM libros WHERE id = ?', (id_libro,))
    libro = cursor.fetchone()
    conn.close()

    if libro:
        info_libro = {
                'id': libro[0],
                'titulo': libro[1],
                'autor': libro[2],
                'año': libro[3],
                'genero': libro[4],
                'disponible': libro[5],
                'portada': libro[6]
            }
        return info_libro
    else:
        print(f"No se encontró información para el ID {id_libro}.")
        return None


def libro_disponible(conn, cursor, id_libro):
    cursor.execute('SELECT disponible FROM libros WHERE id = ?', (id_libro,))
    result = cursor.fetchone()
    if result:
        return result[0] == 1
    else:
        return False

    
def reservar_libro(conn, cursor, id_libro, nombre_usuario):
    cursor.execute('INSERT INTO libros_reservados (id_libro, usuario, fecha_prestamo, devuelto) VALUES (?, ?, DATETIME("now"), 0)', (id_libro, nombre_usuario))
    cursor.execute('UPDATE libros SET disponible = 0 WHERE id = ?', (id_libro,))
    conn.commit()
    print(f"Libro con ID {id_libro} reservado por el usuario {nombre_usuario}.")
    return True


def libros_reservados(conn, cursor, nombre_usuario):
        cursor.execute('''SELECT l.titulo, lr.fecha_prestamo 
                          FROM libros_reservados AS lr 
                          INNER JOIN libros AS l ON lr.id_libro = l.id 
                          WHERE lr.usuario = ? AND lr.devuelto = 0''', (nombre_usuario,))
        libros_reservados = cursor.fetchall()
        if libros_reservados:
            print(f"Libros reservados por el usuario {nombre_usuario}:")
            for reserva in libros_reservados:
                titulo_libro = reserva[0]
                fecha_prestamo = reserva[1]
                
                print(f"Título del libro: {titulo_libro}, Fecha de préstamo: {fecha_prestamo}")
                
            return libros_reservados
        else:
            print(f"No hay libros reservados por el usuario {nombre_usuario}.")
            return []



def devolver_libro(conn, cursor, titulo_libro, nombre_usuario, label):
        # Verificar si el libro está reservado por el usuario
        cursor.execute('SELECT l.id FROM libros AS l INNER JOIN libros_reservados AS lr ON l.id = lr.id_libro WHERE l.titulo = ? AND lr.usuario = ?', (titulo_libro, nombre_usuario))
        id_libro_reservado = cursor.fetchone()

        if id_libro_reservado:
            id_libro = id_libro_reservado[0]
            # Marcar el libro como devuelto y actualizar la disponibilidad
            cursor.execute('UPDATE libros_reservados SET devuelto = 1, fecha_devolucion = DATETIME("now") WHERE id_libro = ? AND usuario = ?', (id_libro, nombre_usuario))
            cursor.execute('UPDATE libros SET disponible = 1 WHERE id = ?', (id_libro,))
            conn.commit()
            print(f"Libro con título '{titulo_libro}' devuelto por el usuario {nombre_usuario}.")
            label.setStyleSheet("QLabel { color : green; }")
            label.setText("Libro devuelto")
            return True
        else:
            print(f"No se encontró ningún libro con el título '{titulo_libro}' reservado.")
            label.setStyleSheet("QLabel { color : red; }")
            label.setText(f"No se encontró el libro '{titulo_libro}' reservado.")
            return False


def hacer_admin(conn, cursor, nombre_usuario):
        cursor.execute('UPDATE usuarios SET administrador = 1 WHERE nombre = ?', (nombre_usuario,))
        conn.commit()
        print(f"El usuario {nombre_usuario} ahora es administrador.")
        return True

    
def listar_usuarios(conn, cursor):
        cursor.execute('SELECT nombre, email, administrador FROM usuarios')
        usuarios = cursor.fetchall()
        if usuarios:
            print("Lista de usuarios:")
            for usuario in usuarios:
                nombre = usuario[0]
                email = usuario[1]
                administrador = "Sí" if usuario[2] == 1 else "No"
                print(f"Nombre: {nombre}, Email: {email}, Administrador: {administrador}")
            return usuarios
        else:
            print("No hay usuarios registrados.")
            return []

    

def eliminar_usuario(conn, cursor, nombre_usuario):
        cursor.execute('DELETE FROM usuarios WHERE nombre = ?', (nombre_usuario,))
        cursor.execute('DELETE FROM usuarios_bloqueados WHERE nombre = ?', (nombre_usuario,))
        conn.commit()
        print(f"Usuario {nombre_usuario} eliminado.")
        return True

    
def bloquear_usuario(conn, cursor, nombre_usuario):
        cursor.execute('INSERT INTO usuarios_bloqueados (nombre) VALUES (?)', (nombre_usuario,))
        conn.commit()
        print(f"Usuario {nombre_usuario} bloqueado.")
        return True

    
def desbloquear_usuario(conn, cursor, nombre_usuario):
        cursor.execute('DELETE FROM usuarios_bloqueados WHERE nombre = ?', (nombre_usuario,))
        conn.commit()
        print(f"Usuario {nombre_usuario} desbloqueado.")
        return True

    
def mostrar_bloqueados(conn, cursor):
        # quiero mostrar tambien el email que esta en la tabla de usuarios
        cursor.execute('SELECT u.nombre, u.email FROM usuarios_bloqueados AS ub INNER JOIN usuarios AS u ON ub.nombre = u.nombre')
        bloqueados = cursor.fetchall()
        if bloqueados:
            print("Usuarios bloqueados:")
            for bloqueado in bloqueados:
                nombre = bloqueado[0]
                email = bloqueado[1]
                print(f"Nombre: {nombre}, Email: {email}")
            return bloqueados
        else:
            print("No hay usuarios bloqueados.")
            return []

    
