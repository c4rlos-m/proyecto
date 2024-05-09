import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from database.database import connect, insert_user, login_user
from plantillas.pantallaPrincipal import Ui_MainWindow as vPrincipal
from plantillas.menuPrincipal import Ui_MainWindow as vMenuPrincipal
from plantillas.paginaAdministrador import Ui_MainWindow as vMenuAdmin

from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget


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

        # Obtén la conexión y el cursor desde la función connect()
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        # si el usuario existe, muestra la pantalla principal
        if login_user(conn, cursor, nombre, password):
            # Oculta la ventana de login
            self.hide()

            # si el usuario es administrador, abrir una pantalla de administrador
            if self.user_is_admin(conn, cursor, nombre):
                print("El usuario es administrador")
                # Crear e iniciar la ventana de administrador
                self.menu_admin = menuAdmin()
                self.menu_admin.show()
            else:
                print("El usuario no es administrador")
                # Crear e iniciar la ventana del menú principal
                self.menu_principal = menuPrincipal()
                self.menu_principal.show()

        # Cerrar la conexión después de su uso
        conn.close()


    

    def register(self):

        nombre = self.ui.usernameInputRegister.text()
        email = self.ui.emailInput.text()
        password = self.ui.passwordInputRegister.text()

        # Obtén la conexión y el cursor desde la función connect()
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        # Llama a la función insert_user() con los parámetros correctos
        insert_user(conn, cursor, nombre, email, password)


class menuPrincipal(QMainWindow, vMenuPrincipal):
    def __init__(self):
        super().__init__()
        self.ui = vMenuPrincipal()
        self.ui.setupUi(self)

class menuAdmin(QMainWindow, vMenuAdmin):
    def __init__(self):
        super().__init__()
        self.ui = vMenuAdmin()
        self.ui.setupUi(self)





    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
