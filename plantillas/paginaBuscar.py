# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paginaBuscar.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"/* Estilos para QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #273746; /* Fondo azul oscuro */\n"
"    color: #ECF0F1; /* Texto blanco */\n"
"    border: 2px solid #3498DB; /* Borde azul */\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    font-size: 16px; /* Tama\u00f1o de letra */\n"
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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 10, 221, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.autorInput = QLineEdit(self.centralwidget)
        self.autorInput.setObjectName(u"autorInput")
        self.autorInput.setGeometry(QRect(120, 70, 281, 51))
        font1 = QFont()
        font1.setBold(True)
        self.autorInput.setFont(font1)
        self.buscarAutor = QPushButton(self.centralwidget)
        self.buscarAutor.setObjectName(u"buscarAutor")
        self.buscarAutor.setGeometry(QRect(490, 70, 111, 51))
        self.buscarAutor.setFont(font1)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(70, 140, 360, 400))
        font2 = QFont()
        font2.setPointSize(18)
        self.graphicsView.setFont(font2)
        self.graphicsView.setStyleSheet(u"border: 1px solid #3498DB;\n"
"border-radius: 5px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(550, 240, 181, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setToolTipDuration(5)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(550, 310, 181, 31))
        self.label_3.setFont(font3)
        self.label_3.setToolTipDuration(5)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(550, 370, 221, 31))
        self.label_4.setFont(font3)
        self.label_4.setToolTipDuration(5)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(670, 10, 111, 41))
        font4 = QFont()
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.logoutButton.setFont(font4)
        self.logoutButton.setStyleSheet(u"background-color: red;\n"
"border-radius: 5px;\n"
"border:  none\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(550, 210, 51, 31))
        self.label_5.setFont(font3)
        self.label_5.setToolTipDuration(5)
        self.label_5.setStyleSheet(u"color:#3498DB")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(550, 280, 51, 31))
        self.label_6.setFont(font3)
        self.label_6.setToolTipDuration(5)
        self.label_6.setStyleSheet(u"color:#3498DB")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(550, 340, 221, 31))
        self.label_7.setFont(font3)
        self.label_7.setToolTipDuration(5)
        self.label_7.setStyleSheet(u"color:#3498DB")
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"BUSCAR UN LIBRO", None))
        self.autorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por Titulo", None))
        self.buscarAutor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Titulo:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o Publicacion:", None))
    # retranslateUi

