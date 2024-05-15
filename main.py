import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from database.database import connect, insert_user, login_user, title_to_id, obtener_info_libro_por_id, libro_disponible, reservar_libro
from plantillas.pantallaPrincipal import Ui_MainWindow as vPrincipal
from plantillas.menuPrincipal import Ui_MainWindow as vMenuPrincipal
from plantillas.paginaAdministrador import Ui_MainWindow as vMenuAdmin
from plantillas.paginaReservar import Ui_MainWindow as vReservar
from plantillas.paginaBuscar import Ui_MainWindow as vBuscar
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget, QTableWidgetItem, QGraphicsScene, QSizePolicy, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, Qt


class MainWindow(QMainWindow, vPrincipal):
    def __init__(self):
        super().__init__()
        self.ui = vPrincipal()
        self.ui.setupUi(self)
        self.ui.registerButtonPage.clicked.connect(self.show_register_page)
        self.ui.loginButtonPage.clicked.connect(self.show_login_page)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        connect()


    def show_register_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_login_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def user_is_admin(self, conn, cursor, nombre):
        try:
            cursor.execute('SELECT * FROM usuarios WHERE nombre = ? AND administrador = 1', (nombre,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print("Error al verificar si el usuario es administrador:", e)
            return False

    def login(self):
        nombre = self.ui.usernameInputLogin.text()
        password = self.ui.passwordInputLogin.text()

        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        if login_user(conn, cursor, nombre, password):
            self.hide()
            if self.user_is_admin(conn, cursor, nombre):
                print("El usuario es administrador")
                self.menu_admin = menuAdmin()
                self.menu_admin.show()
            else:
                print("El usuario no es administrador")
                self.menu_principal = menuPrincipal(self)
                self.menu_principal.show()
        self.ui.usernameInputLogin.clear()
        self.ui.passwordInputLogin.clear()
        conn.close()

    def register(self):
        nombre = self.ui.usernameInputRegister.text()
        email = self.ui.emailInput.text()
        password = self.ui.passwordInputRegister.text()

        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        insert_user(conn, cursor, nombre, email, password)

        # Limpia los campos de entrada de texto
        self.ui.usernameInputRegister.clear()
        self.ui.emailInput.clear()
        self.ui.passwordInputRegister.clear()

        conn.close()


# PAGINA PRINCIPAL USUARIOS DESPUES DE LOGEARSE
class menuPrincipal(QMainWindow, vMenuPrincipal):
    def __init__(self, main_window):
        super().__init__()
        self.ui = vMenuPrincipal()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.show_data()
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.buscarButton.clicked.connect(self.pagina_buscar)
        self.ui.ReservarButton.clicked.connect(self.pagina_reservar)    

    def show_data(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        query = 'SELECT * FROM libros'
        cursor.execute(query)
        libros = cursor.fetchall()

        conn.close()

        self.ui.tablaLibros.setRowCount(len(libros))
        for row_number, row_data in enumerate(libros):
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.tablaLibros.setItem(row_number, column_number, item)

    def logout(self):
        self.close()
        self.main_window.show()

    def pagina_buscar(self):
        self.hide()  # Oculta la ventana actual
        # Crea una instancia de la ventana de búsqueda
        self.pagina_buscar_window = PaginaBuscar(self)  # Cambio de nombre de la variable
        # Muestra la ventana de búsqueda
        self.pagina_buscar_window.show()

    def pagina_reservar(self):
        self.hide()
        self.pagina_reservar_window = PaginaReservar(self)
        self.pagina_reservar_window.show()



# PAGINA ADMINISTRADOR
class menuAdmin(QMainWindow, vMenuAdmin):
    def __init__(self):
        super().__init__()
        self.ui = vMenuAdmin()
        self.ui.setupUi(self)


# PAGINA BUSCAR LIBRO
class PaginaBuscar(QMainWindow, vBuscar):
    def __init__(self, main_window):
        super().__init__()
        self.ui = vBuscar()
        self.ui.setupUi(self)  # Pasar self al setupUi
        self.main_window = main_window
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.buscarAutor.clicked.connect(self.buscar_libro)  # Conectar la señal clicked al método buscar_libro

        # Llamar al método mostrar_imagen con la ruta de la imagen por defecto
        self.mostrar_imagen('./src/libros.png')

    def mostrar_imagen(self, ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene = QGraphicsScene()
        scene.addItem(pixmap_item)
        
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)
        self.ui.graphicsView.setAlignment(Qt.AlignCenter)
        self.ui.graphicsView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Los otros métodos permanecen sin cambios

    def libro_no_encontrado(self):
        self.ui.label_2.setText("Libro no encontrado")
        self.ui.label_3.setText("")
        self.ui.label_4.setText("")
        self.mostrar_imagen('./src/no_encontrado.png')


    def mostrar_info_libro(self, info_libro):
        self.ui.label_2.setText(info_libro['titulo'])
        self.ui.label_3.setText(info_libro['autor'])
        self.ui.label_4.setText(str(info_libro['año']))

    def buscar_libro(self):
        titulo_libro = self.ui.autorInput.text()
        self.ui.autorInput.clear()
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        id_libro = title_to_id(conn, cursor, titulo_libro)
        conn.close()

        if id_libro is not None:
            print("Libro encontrado")
            info_libro = obtener_info_libro_por_id(id_libro)  # Pasar el id_libro como argumento
            if info_libro:
                print(info_libro)
                self.mostrar_imagen(info_libro['portada'])
                self.mostrar_info_libro(info_libro)
            else:
                print("Información del libro no encontrada.")
                self.libro_no_encontrado()
        else:
            print("Libro no encontrado")
            self.libro_no_encontrado()

    def logout(self):
        self.close()
        self.main_window.show()



class PaginaReservar(QMainWindow, vReservar):
    def __init__(self, main_window):
        super().__init__()
        self.ui = vReservar()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.buscarAutor.clicked.connect(self.buscar_libro)  # Conectar la señal clicked al método buscar_libro
        self.ui.pushButton.clicked.connect(self.reservar_libro)  # Conectar la señal clicked al método reservar_libro
        # Llamar al método mostrar_imagen con la ruta de la imagen por defecto
        self.mostrar_imagen('./src/libros.png')

    def mostrar_imagen(self, ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene = QGraphicsScene()
        scene.addItem(pixmap_item)
        
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)
        self.ui.graphicsView.setAlignment(Qt.AlignCenter)
        self.ui.graphicsView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    # Los otros métodos permanecen sin cambios

    def libro_no_encontrado(self):
        self.ui.label_2.setText("Libro no encontrado")
        self.ui.label_3.setText("")
        self.ui.label_4.setText("")
        self.mostrar_imagen('./src/no_encontrado.png')


    def mostrar_info_libro(self, info_libro):
        self.ui.label_2.setText(info_libro['titulo'])
        self.ui.label_3.setText(info_libro['autor'])
        self.ui.label_4.setText(str(info_libro['año']))

    def buscar_libro(self):
        titulo_libro = self.ui.autorInput.text()
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        id_libro = title_to_id(conn, cursor, titulo_libro)
        conn.close()

        if id_libro is not None:
            print("Libro encontrado")
            info_libro = obtener_info_libro_por_id(id_libro)  # Pasar el id_libro como argumento
            if info_libro:
                print(info_libro)
                self.mostrar_imagen(info_libro['portada'])
                self.mostrar_info_libro(info_libro)
                return titulo_libro
            else:
                print("Información del libro no encontrada.")
                self.libro_no_encontrado()
        else:
            print("Libro no encontrado")
            self.libro_no_encontrado()
        

    def libro_disponible(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        titulo_libro = self.ui.autorInput.text()
        id_libro = title_to_id(conn, cursor, titulo_libro)
        disponible = libro_disponible(conn, cursor, id_libro)
        conn.close()
        return disponible
    
    def reservar_libro(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        libro_id = title_to_id(conn, cursor, self.ui.autorInput.text())
        if self.libro_disponible():
            print("Libro reservado")
            reservar_libro(conn, cursor, libro_id, "usuario")
            self.ui.label_8.setText("Libro reservado")
        else:
            print("Libro no disponible")
            self.ui.label_8.setText("Libro no disponible")

    def logout(self):
        self.close()
        self.main_window.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


 