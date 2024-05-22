# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuPrincipal.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 603)
        MainWindow.setStyleSheet(u"\n"
"\n"
"/* Estilos para la etiqueta de bienvenida */\n"
"QLabel#label {\n"
"    font-size: 20px; /* Tama\u00f1o de fuente */\n"
"    color: white; /* Color de texto */\n"
"}\n"
"\n"
"/* Estilos para los botones */\n"
"QPushButton#buscarButton,\n"
"QPushButton#DevolverButton,\n"
"QPushButton#ReservarButton {\n"
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
"QPushButton#buscarButton:hover,\n"
"QPushButton#DevolverButton:hover,\n"
"QPushButton#ReservarButton:hover {\n"
"    background-color: #4A58E7; /* Cambiar color al pasar el rat\u00f3n */\n"
"}\n"
"\n"
"/* Estilos para la tabla */\n"
"QTableWidget#tableWidget {\n"
"    background-color: #fff; /* Color de"
                        " fondo */\n"
"    border: 2px solid #ddd; /* Borde */\n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QTableWidget#tableWidget::item {\n"
"    padding: 5px; /* Espaciado interno */\n"
"}\n"
"\n"
"QTableWidget#tableWidget::item:selected {\n"
"    background-color: #e0e0e0; /* Color de fondo de la selecci\u00f3n */\n"
"}\n"
"\n"
"/* Estilos para la etiqueta de libros disponibles */\n"
"QLabel#label_2 {\n"
"    font-size: 16px; /* Tama\u00f1o de fuente */\n"
"    color: white; /* Color de texto */\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 70, 341, 21))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.buscarButton = QPushButton(self.centralwidget)
        self.buscarButton.setObjectName(u"buscarButton")
        self.buscarButton.setGeometry(QRect(180, 160, 101, 41))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.buscarButton.setFont(font1)
        self.tablaLibros = QTableWidget(self.centralwidget)
        if (self.tablaLibros.columnCount() < 4):
            self.tablaLibros.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tablaLibros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tablaLibros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tablaLibros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tablaLibros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tablaLibros.rowCount() < 5):
            self.tablaLibros.setRowCount(5)
        self.tablaLibros.setObjectName(u"tablaLibros")
        self.tablaLibros.setGeometry(QRect(80, 290, 631, 181))
        self.tablaLibros.setMinimumSize(QSize(631, 0))
        self.tablaLibros.setSortingEnabled(False)
        self.tablaLibros.setRowCount(5)
        self.tablaLibros.horizontalHeader().setDefaultSectionSize(153)
        self.tablaLibros.horizontalHeader().setStretchLastSection(False)
        self.DevolverButton = QPushButton(self.centralwidget)
        self.DevolverButton.setObjectName(u"DevolverButton")
        self.DevolverButton.setGeometry(QRect(500, 160, 111, 41))
        self.DevolverButton.setFont(font1)
        self.ReservarButton = QPushButton(self.centralwidget)
        self.ReservarButton.setObjectName(u"ReservarButton")
        self.ReservarButton.setGeometry(QRect(340, 160, 111, 41))
        self.ReservarButton.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 250, 141, 21))
        self.label_2.setFont(font)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(330, 520, 111, 41))
        self.logoutButton.setFont(font1)
        self.logoutButton.setStyleSheet(u"background-color: red;\n"
"border-radius: 5px\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 30, 251, 91))
        self.label_3.setStyleSheet(u"image: url(./src/les_salines.png);")
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bienvenid@ a la biblioteca de M3", None))
        self.buscarButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem = self.tablaLibros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem1 = self.tablaLibros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem2 = self.tablaLibros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fecha Publicaci\u00f3n", None));
        ___qtablewidgetitem3 = self.tablaLibros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Genero", None));
        self.DevolverButton.setText(QCoreApplication.translate("MainWindow", u"Devolver", None))
        self.ReservarButton.setText(QCoreApplication.translate("MainWindow", u"Reservar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Proximas Entregas", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_3.setText("")
    # retranslateUi

