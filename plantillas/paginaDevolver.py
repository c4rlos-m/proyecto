# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paginaDevolver.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

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
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 290, 401, 211))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setBaseSize(QSize(0, 0))
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 370, 311, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #3498DB")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 20, 241, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.logoutButton = QPushButton(self.centralwidget)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(630, 20, 111, 41))
        font2 = QFont()
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.logoutButton.setFont(font2)
        self.logoutButton.setStyleSheet(u"background-color: red;\n"
"border-radius: 5px;\n"
"border:  none\n"
"")
        self.autorInput = QLineEdit(self.centralwidget)
        self.autorInput.setObjectName(u"autorInput")
        self.autorInput.setGeometry(QRect(80, 110, 281, 51))
        font3 = QFont()
        font3.setBold(True)
        self.autorInput.setFont(font3)
        self.buscarAutor = QPushButton(self.centralwidget)
        self.buscarAutor.setObjectName(u"buscarAutor")
        self.buscarAutor.setGeometry(QRect(430, 110, 111, 51))
        self.buscarAutor.setFont(font3)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 250, 181, 16))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_3.setFont(font4)
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
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha Reserva", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quieres devolver alg\u00fan libro?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DEVOLVER UN LIBRO", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Volver", None))
        self.autorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por Titulo", None))
        self.buscarAutor.setText(QCoreApplication.translate("MainWindow", u"Devolver", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tus libros Reservados", None))
    # retranslateUi

