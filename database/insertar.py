import sqlite3
import random
import datetime

# Función para insertar datos de prueba
def insertar_datos_de_prueba():
    # Conexión a la base de datos
    conexion = sqlite3.connect('biblioteca.db')
    cursor = conexion.cursor()

    # Lista de títulos, autores y géneros de ejemplo
    titulos = ["Cien años de soledad", "El señor de los anillos", "Harry Potter y la piedra filosofal", "1984",
               "Don Quijote de la Mancha", "Orgullo y prejuicio", "El principito", "Matar a un ruiseñor", "El gran Gatsby",
               "El hobbit", "Crimen y castigo", "Rayuela", "El alquimista", "Los miserables", "El código Da Vinci",
               "La sombra del viento", "El nombre del viento", "Anna Karenina", "La Odisea", "Hamlet"]
    autores = ["Gabriel García Márquez", "J.R.R. Tolkien", "J.K. Rowling", "George Orwell", "Miguel de Cervantes",
               "Jane Austen", "Antoine de Saint-Exupéry", "Harper Lee", "F. Scott Fitzgerald", "J.R.R. Tolkien",
               "Fiódor Dostoievski", "Julio Cortázar", "Paulo Coelho", "Victor Hugo", "Dan Brown", "Carlos Ruiz Zafón",
               "Patrick Rothfuss", "Lev Tolstói", "Homero", "William Shakespeare"]
    generos = ["Ficción", "Fantasía", "Aventura", "Ciencia ficción", "Clásico", "Romance", "Infantil", "Drama", "Suspenso"]

    # Insertar 20 datos de prueba
    for _ in range(20):
        titulo = random.choice(titulos)
        autor = random.choice(autores)
        fecha_publicacion = datetime.date(random.randint(1900, 2022), random.randint(1, 12), random.randint(1, 28)).isoformat()
        genero = random.choice(generos)
        disponible = random.randint(0, 1)
        
        cursor.execute('''INSERT INTO libros (titulo, autor, fecha_publicacion, genero, disponible)
                          VALUES (?, ?, ?, ?, ?)''', (titulo, autor, fecha_publicacion, genero, disponible))

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

# Llamar a la función para insertar datos de prueba
insertar_datos_de_prueba()
