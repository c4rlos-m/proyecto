# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantallaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 575)
        MainWindow.setStyleSheet(u"/* Estilos para QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #273746; /* Fondo azul oscuro */\n"
"    color: #ECF0F1; /* Texto blanco */\n"
"    border: 2px solid #3498DB; /* Borde azul */\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-size: 16px; /* Tama\u00f1o de letra */\n"
"    text-align: center; /* Texto centrado */\n"
"}\n"
"\n"
"/* Estilos para QPushButton */\n"
"QPushButton {\n"
"    background-color: #3498DB; /* Fondo azul */\n"
"    color: #ECF0F1; /* Texto blanco */\n"
"    border: 2px solid #3498DB; /* Borde azul */\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px; /* Ajuste del padding */\n"
"    font-size: 16px; /* Tama\u00f1o de letra */\n"
"    text-align: center; /* Texto centrado */\n"
"}\n"
"\n"
"/* Estilos para QPushButton al pasar el mouse */\n"
"QPushButton:hover {\n"
"    background-color: #2980B9; /* Fondo azul oscuro al pasar el mouse */\n"
"}\n"
"\n"
"/* Estilos para QPushButton al hacer clic */\n"
"QPushButton:pressed {\n"
"    background-color: #1F6"
                        "18D; /* Fondo azul m\u00e1s oscuro al hacer clic */\n"
"}\n"
"\n"
"/* Alineaci\u00f3n central para todos los widgets */\n"
"QWidget {\n"
"    text-align: center;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 30, 751, 481))
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.usernameInputLogin = QLineEdit(self.loginPage)
        self.usernameInputLogin.setObjectName(u"usernameInputLogin")
        self.usernameInputLogin.setGeometry(QRect(260, 130, 251, 41))
        self.passwordInputLogin = QLineEdit(self.loginPage)
        self.passwordInputLogin.setObjectName(u"passwordInputLogin")
        self.passwordInputLogin.setGeometry(QRect(260, 190, 251, 41))
        self.loginButton = QPushButton(self.loginPage)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(320, 270, 131, 51))
        font = QFont()
        font.setBold(True)
        self.loginButton.setFont(font)
        self.label = QLabel(self.loginPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 50, 181, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.loginPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 360, 171, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.registerButtonPage = QPushButton(self.loginPage)
        self.registerButtonPage.setObjectName(u"registerButtonPage")
        self.registerButtonPage.setGeometry(QRect(400, 340, 121, 51))
        self.registerButtonPage.setFont(font)
        self.stackedWidget.addWidget(self.loginPage)
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.emailInput = QLineEdit(self.registerPage)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(260, 130, 251, 41))
        self.usernameInputRegister = QLineEdit(self.registerPage)
        self.usernameInputRegister.setObjectName(u"usernameInputRegister")
        self.usernameInputRegister.setGeometry(QRect(260, 190, 251, 41))
        self.passwordInputRegister = QLineEdit(self.registerPage)
        self.passwordInputRegister.setObjectName(u"passwordInputRegister")
        self.passwordInputRegister.setGeometry(QRect(260, 250, 251, 41))
        self.registerButton = QPushButton(self.registerPage)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(290, 320, 161, 51))
        self.registerButton.setFont(font)
        self.label_3 = QLabel(self.registerPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 410, 161, 21))
        self.label_3.setFont(font2)
        self.loginButtonPage = QPushButton(self.registerPage)
        self.loginButtonPage.setObjectName(u"loginButtonPage")
        self.loginButtonPage.setGeometry(QRect(420, 400, 141, 51))
        self.loginButtonPage.setFont(font)
        self.label_4 = QLabel(self.registerPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 50, 221, 51))
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.registerPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usernameInputLogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInputLogin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"No tienes cuenta?", None))
        self.registerButtonPage.setText(QCoreApplication.translate("MainWindow", u"Registrate", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.usernameInputRegister.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInputRegister.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ya tienes cuenta?", None))
        self.loginButtonPage.setText(QCoreApplication.translate("MainWindow", u"Inicia Sesion", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
    # retranslateUi

