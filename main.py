import sys
from database.database import Database 
from PySide6.QtWidgets import QApplication, QMainWindow
from plantillas.pantallaPrincipal import Ui_MainWindow 

from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.registerButtonPage.clicked.connect(self.show_register_page)
        self.ui.loginButtonPage.clicked.connect(self.show_login_page)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)

    def show_register_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_login_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def login(self):
        # Aquí puedes implementar la lógica para el inicio de sesión
        # Por ejemplo, obtener los datos de los QLineEdit y procesarlos
        # Una vez iniciada la sesión, puedes alternar a la página de inicio
        print("Iniciado sesión")

    def register(self):
        # Aquí puedes implementar la lógica para el registro
        # Por ejemplo, obtener los datos de los QLineEdit y procesarlos
        # Una vez registrado, puedes alternar a la página de inicio de sesión
        print("Registrado")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
