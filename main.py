import sqlite3
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from database.database import connect, insert_user, login_user, title_to_id, obtener_info_libro_por_id, libro_disponible, reservar_libro, libros_reservados, devolver_libro, hacer_admin, listar_usuarios, eliminar_usuario, bloquear_usuario, desbloquear_usuario, mostrar_bloqueados
from plantillas.pantallaPrincipal import Ui_MainWindow as vPrincipal
from plantillas.menuPrincipal import Ui_MainWindow as vMenuPrincipal
from plantillas.paginaAdministrador import Ui_MainWindow as vMenuAdmin
from plantillas.paginaReservar import Ui_MainWindow as vReservar
from plantillas.paginaBuscar import Ui_MainWindow as vBuscar
from plantillas.paginaDevolver import Ui_MainWindow as vDevolver
from PySide6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QWidget, QTableWidgetItem, QGraphicsScene, QSizePolicy, QGraphicsPixmapItem, QHeaderView
from PySide6.QtGui import QPixmap, Qt, QIcon




class MainWindow(QMainWindow, vPrincipal):
    def __init__(self):
        super().__init__()
        self.ui = vPrincipal()
        self.ui.setupUi(self)
        self.ui.registerButtonPage.clicked.connect(self.show_register_page)
        self.ui.loginButtonPage.clicked.connect(self.show_login_page)
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        self.setWindowTitle("M3 Biblioteca")
        self.setWindowIcon(QIcon("./src/libros.png"))

        connect()

    # Método para mostrar la página de registro
    def show_register_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    # Método para mostrar la página de inicio de sesión
    def show_login_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    # Metodo para comprobar si un usuario es administrador
    def user_is_admin(self, conn, cursor, nombre):
            cursor.execute('SELECT * FROM usuarios WHERE nombre = ? AND administrador = 1', (nombre,))
            return cursor.fetchone() is not None

    # Método para iniciar sesión
    def login(self):
        nombre = self.ui.usernameInputLogin.text()
        password = self.ui.passwordInputLogin.text()

        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        # Llamar a la función login_user en database.py
        if login_user(conn, cursor, nombre, password):
            self.hide()
            global usuario_logeado # Variable global para almacenar el nombre del usuario logeado para usar despues en la reserva de libros
            usuario_logeado = nombre
            if self.user_is_admin(conn, cursor, nombre):
                print("El usuario es administrador")
                self.menu_admin = menuAdmin(self)
                self.menu_admin.show()
            else:
                print("El usuario no es administrador")
                self.menu_principal = menuPrincipal(self)
                self.menu_principal.show()
        self.ui.usernameInputLogin.clear()
        self.ui.passwordInputLogin.clear()
        conn.close()
    # Método para registrar un usuario
    def register(self):
        nombre = self.ui.usernameInputRegister.text()
        email = self.ui.emailInput.text()
        password = self.ui.passwordInputRegister.text()

        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        # Llamar a la función insert_user en database.py para insertar el usuario en la tabla usuarios
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
        self.show_data()  # Llamar al método show_data para mostrar los libros en la tabla
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.buscarButton.clicked.connect(self.pagina_buscar)
        self.ui.ReservarButton.clicked.connect(self.pagina_reservar) 
        self.ui.DevolverButton.clicked.connect(self.pagina_devolver)   

    def show_data(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        query = 'SELECT * FROM proximos_libros'
        cursor.execute(query)
        libros = cursor.fetchall()

        conn.close()

        self.ui.tablaLibros.setRowCount(len(libros))
        for row_number, row_data in enumerate(libros):
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.tablaLibros.setItem(row_number, column_number, item)
    # Metodo para hacer logout
    def logout(self):
        self.close()
        self.main_window.show()
    # Metodo para mostrar la pagina de busqueda, solo oculta la ventana actual y muestra la de busqueda
    def pagina_buscar(self):
        self.hide()  # Oculta la ventana actual
        # Crea una instancia de la ventana de búsqueda
        self.pagina_buscar_window = PaginaBuscar(self)  # Cambio de nombre de la variable
        # Muestra la ventana de búsqueda
        self.pagina_buscar_window.show()
    # Metodo para mostrar la pagina de reservar, solo oculta la ventana actual y muestra la de reservar
    def pagina_reservar(self):
        self.hide()
        self.pagina_reservar_window = PaginaReservar(self)
        self.pagina_reservar_window.show()
    # Metodo para mostrar la pagina de devolver, solo oculta la ventana actual y muestra la de devolver
    def pagina_devolver(self):
        self.hide()
        self.pagina_devolver_window = PaginaDevolver(self)
        self.pagina_devolver_window.show()


# PAGINA ADMINISTRADOR
class menuAdmin(QMainWindow, vMenuAdmin):
    def __init__(self, main_window):
        super().__init__()
        self.ui = vMenuAdmin()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.listar_usuarios()
        self.mostrar_bloqueados()
        self.ui.pushButton.clicked.connect(self.hacer_admin)
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.pushButton_4.clicked.connect(self.eliminar_usuario)
        self.ui.pushButton_2.clicked.connect(self.bloquear_usuario)
        self.ui.pushButton_3.clicked.connect(self.desbloquear_usuario)

    # Metodo para listar los usuarios en la tabla 
    def listar_usuarios(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        usuarios = listar_usuarios(conn, cursor)
        conn.close()

        self.ui.tableWidget.setRowCount(len(usuarios))
        for row_number, row_data in enumerate(usuarios):
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.tableWidget.setItem(row_number, column_number, item)
        # Establecer el ancho de la primera columna más grande
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
    
    def hacer_admin(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        hacer_admin(conn, cursor, self.ui.lineEdit.text())
        conn.close()
        self.listar_usuarios()

    def eliminar_usuario(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        eliminar_usuario(conn, cursor, self.ui.lineEdit.text())
        conn.close()
        self.listar_usuarios()
        self.mostrar_bloqueados()

    def mostrar_bloqueados(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        bloqueados = mostrar_bloqueados(conn, cursor)
        conn.close()

        self.ui.tableWidget_2.setRowCount(len(bloqueados))
        for row_number, row_data in enumerate(bloqueados):
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.tableWidget_2.setItem(row_number, column_number, item)
        # Establecer el ancho de la primera columna más grande
        header = self.ui.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)



    def bloquear_usuario(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        bloquear_usuario(conn, cursor, self.ui.lineEdit.text())
        conn.close()
        self.mostrar_bloqueados()

    def desbloquear_usuario(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        desbloquear_usuario(conn, cursor, self.ui.lineEdit.text())
        conn.close()
        self.mostrar_bloqueados()

    def logout(self):
        self.close()
        self.main_window.show()


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
            self.ui.label_5.setText("Titulo:")
            self.ui.label_6.setText("Autor:")
            self.ui.label_7.setText("Año Publicación: ")
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
            self.ui.label_5.setText("")
            self.ui.label_6.setText("")
            self.ui.label_7.setText("")
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
        
        if id_libro is not None:
            print("Libro encontrado")
            self.ui.label_5.setText("Titulo:")
            self.ui.label_6.setText("Autor:")
            self.ui.label_7.setText("Año Publicación: ")
            info_libro = obtener_info_libro_por_id(id_libro)
            if info_libro:
                print(info_libro)
                self.mostrar_imagen(info_libro['portada'])
                self.mostrar_info_libro(info_libro)
                
                # Verificar si el libro está disponible
                if libro_disponible(conn, cursor, id_libro):
                    self.ui.label_8.setStyleSheet("QLabel { color : green; }")
                    self.ui.label_8.setText("Disponible")
                else:
                    self.ui.label_8.setStyleSheet("QLabel { color : red; }")
                    self.ui.label_8.setText("No disponible")
                
                conn.close()
                return titulo_libro
            else:
                print("Información del libro no encontrada.")
                self.libro_no_encontrado()
        else:
            print("Libro no encontrado")
            self.ui.label_8.setText("")
            self.ui.label_5.setText("")
            self.ui.label_6.setText("")
            self.ui.label_7.setText("")
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
            reservar_libro(conn, cursor, libro_id, usuario_logeado)
            self.ui.label_8.setStyleSheet("QLabel { color : green;}")
            self.ui.label_8.setText("Libro reservado")
        else:
            print("Libro no disponible")
            self.ui.label_8.setStyleSheet("QLabel { color : red;}")
            self.ui.label_8.setText("No se puede reservar.")

    def logout(self):
        self.close()
        self.main_window.show()


# PAGINA DEVOLVER LIBROS:
class PaginaDevolver(QMainWindow, vDevolver):
    def __init__(self, main_window):
        super().__init__()
        self.ui = vDevolver()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.buscarAutor.clicked.connect(self.devolver_libro)
        self.show_data()
    
    def show_data(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        libros = libros_reservados(conn, cursor, usuario_logeado)
        conn.close()

        self.ui.tableWidget.setRowCount(len(libros))
        for row_number, row_data in enumerate(libros):
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.ui.tableWidget.setItem(row_number, column_number, item)
        if self.ui.tableWidget.rowCount() == 0:
            self.ui.label.setStyleSheet("QLabel { color : red; }")
            self.ui.label.setText("No tienes libros reservados")
        # Establecer el ancho de la primera columna más grande
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # Establecer la primera columna para que se ajuste al contenido
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Establecer la segunda columna para ajustarse al contenido

    def devolver_libro(self):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        devolver_libro(conn, cursor, self.ui.autorInput.text(), usuario_logeado, self.ui.label)
        # if devolver_libro:
        #     self.ui.label.setStyleSheet("QLabel { color : green; }")
        #     self.ui.label.setText("Libro devuelto")
        # else:
        #     self.ui.label.setStyleSheet("QLabel { color : red; }")
        #     self.ui.label.setText("Error al devolver el libro")
        conn.close()
        self.show_data()


    

    def logout(self):
        self.close()
        self.main_window.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


 