# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paginaReservar.ui'
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(650, 10, 111, 41))
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet(u"background-color: red;\n"
"border-radius: 5px;\n"
"border:  none\n"
"")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(450, 270, 221, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_7.setToolTipDuration(5)
        self.label_7.setStyleSheet(u"color:#3498DB")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 240, 181, 31))
        self.label_3.setFont(font1)
        self.label_3.setToolTipDuration(5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 241, 31))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 300, 221, 31))
        self.label_4.setFont(font1)
        self.label_4.setToolTipDuration(5)
        self.autorInput = QLineEdit(self.centralwidget)
        self.autorInput.setObjectName(u"autorInput")
        self.autorInput.setGeometry(QRect(100, 70, 281, 51))
        font3 = QFont()
        font3.setBold(True)
        self.autorInput.setFont(font3)
        self.buscarAutor = QPushButton(self.centralwidget)
        self.buscarAutor.setObjectName(u"buscarAutor")
        self.buscarAutor.setGeometry(QRect(470, 70, 111, 51))
        self.buscarAutor.setFont(font3)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 140, 51, 31))
        self.label_5.setFont(font1)
        self.label_5.setToolTipDuration(5)
        self.label_5.setStyleSheet(u"color:#3498DB")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(450, 210, 51, 31))
        self.label_6.setFont(font1)
        self.label_6.setToolTipDuration(5)
        self.label_6.setStyleSheet(u"color:#3498DB")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(50, 140, 360, 400))
        font4 = QFont()
        font4.setPointSize(18)
        self.graphicsView.setFont(font4)
        self.graphicsView.setStyleSheet(u"border: 1px solid #3498DB;\n"
"border-radius: 5px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 170, 181, 31))
        self.label_2.setFont(font1)
        self.label_2.setToolTipDuration(5)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(490, 380, 231, 16))
        font5 = QFont()
        font5.setPointSize(13)
        self.label_8.setFont(font5)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 450, 91, 41))
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
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o Publicacion:", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"RESERVAR UN LIBRO", None))
        self.label_4.setText("")
        self.autorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por Titulo", None))
        self.buscarAutor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Titulo:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.label_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Disponible // No Disponible", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reservar", None))
    # retranslateUi

