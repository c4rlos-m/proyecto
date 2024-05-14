import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from database.database import connect, insert_user, login_user
from plantillas.pantallaPrincipal import Ui_MainWindow as vPrincipal
from plantillas.menuPrincipal import Ui_MainWindow as vMenuPrincipal
from plantillas.paginaAdministrador import Ui_MainWindow as vMenuAdmin
from plantillas.paginaBuscar import Ui_MainWindow as vBuscar
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget, QTableWidgetItem


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



class menuPrincipal(QMainWindow, vMenuPrincipal):
    def __init__(self, main_window):
        super().__init__()
        self.ui = vMenuPrincipal()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.show_data()
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.buscarButton.clicked.connect(self.pagina_buscar)


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
        self.main_window.show()
        self.close()

    def pagina_buscar(self):
        self.hide()  # Oculta la ventana actual
        # Crea una instancia de la ventana de búsqueda
        self.pagina_buscar = PaginaBuscar()
        # Muestra la ventana de búsqueda
        self.pagina_buscar.show()


    def logout(self):
        # Cierra la ventana actual
        self.close()

        # Abre la ventana de inicio de sesión
        self.main_window = MainWindow()
        self.main_window.show()

class menuAdmin(QMainWindow, vMenuAdmin):
    def __init__(self):
        super().__init__()
        self.ui = vMenuAdmin()
        self.ui.setupUi(self)

class PaginaBuscar(QMainWindow, vBuscar):
    def __init__(self, main_window):
        super().__init__()
        self.ui = vBuscar()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.logoutButton.clicked.connect(self.logout)

    def logout(self):
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


 