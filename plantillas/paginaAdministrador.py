# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paginaAdministrador.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"/* Estilos para la etiqueta de bienvenida */\n"
"QLabel#label {\n"
"    font-size: 20px; /* Tama\u00f1o de fuente */\n"
"    color: white; /* Color de texto */\n"
"}\n"
"\n"
"/* Estilos para los botones */\n"
"QPushButton#pushButton,\n"
"QPushButton#pushButton_2,\n"
"QPushButton#pushButton_3,\n"
"QPushButton#pushButton_4 {\n"
"    background-color: #3498DB; /* Color de fondo */\n"
"    color: white; /* Color de texto */\n"
"    border-radius: 5px; \n"
"    padding: 8px 16px; /* Espaciado interno */\n"
"    text-align: center; /* Alineaci\u00f3n de texto */\n"
"    text-decoration: none; /* Sin decoraci\u00f3n de texto */\n"
"    font-size: 16px; /* Tama\u00f1o de fuente */\n"
"    margin: 4px 2px; /* Margen */\n"
"}\n"
"\n"
"QPushButton#pushButton:hover,\n"
"QPushButton#pushButton_2:hover,\n"
"QPushButton#pushButton_3:hover,\n"
"QPushButton#pushButton_4:hover {\n"
"    background-color: #4A58E7; /* Cambiar color al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #273746; /* Fondo az"
                        "ul oscuro */\n"
"    color: #ECF0F1; /* Texto blanco */\n"
"    border: 2px solid #3498DB; /* Borde azul */\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-size: 16px; /* Tama\u00f1o de letra */\n"
"    text-align: center; /* Texto centrado */\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 0, 301, 101))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(640, 30, 121, 41))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.logoutButton.setFont(font1)
        self.logoutButton.setStyleSheet(u"background-color: red;\n"
"border-radius: 5px;\n"
"border:  none\n"
"")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 310, 341, 211))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget_2 = QTableWidget(self.centralwidget)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        if (self.tableWidget_2.rowCount() < 10):
            self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(460, 310, 281, 211))
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(120)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 280, 61, 16))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 280, 181, 20))
        self.label_3.setFont(font2)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(270, 103, 311, 41))
        self.lineEdit.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 190, 191, 51))
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(304, 190, 121, 51))
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(450, 190, 131, 51))
        self.pushButton_3.setFont(font1)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(604, 190, 111, 51))
        self.pushButton_4.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ventana Administrador", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Administrador", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuarios Bloqueados", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Introducir Usuario", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Hacer Administrador", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Bloquear", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Desbloquear", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

