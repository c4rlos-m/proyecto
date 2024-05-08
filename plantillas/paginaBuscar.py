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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

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
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tablalibrosbuscar = QTableWidget(self.centralwidget)
        if (self.tablalibrosbuscar.columnCount() < 6):
            self.tablalibrosbuscar.setColumnCount(6)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tablalibrosbuscar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tablalibrosbuscar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tablalibrosbuscar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tablalibrosbuscar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tablalibrosbuscar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tablalibrosbuscar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tablalibrosbuscar.setObjectName(u"tablalibrosbuscar")
        self.tablalibrosbuscar.setGeometry(QRect(90, 230, 631, 251))
        self.tablalibrosbuscar.setMinimumSize(QSize(631, 0))
        self.tablalibrosbuscar.setSortingEnabled(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 50, 221, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.autorInput = QLineEdit(self.centralwidget)
        self.autorInput.setObjectName(u"autorInput")
        self.autorInput.setGeometry(QRect(170, 120, 281, 51))
        self.autorInput.setFont(font)
        self.buscarAutor = QPushButton(self.centralwidget)
        self.buscarAutor.setObjectName(u"buscarAutor")
        self.buscarAutor.setGeometry(QRect(490, 120, 111, 51))
        self.buscarAutor.setFont(font)
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
        ___qtablewidgetitem = self.tablalibrosbuscar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tablalibrosbuscar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"titulo", None));
        ___qtablewidgetitem2 = self.tablalibrosbuscar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"autor", None));
        ___qtablewidgetitem3 = self.tablalibrosbuscar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o Publicacion", None));
        ___qtablewidgetitem4 = self.tablalibrosbuscar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"genero", None));
        ___qtablewidgetitem5 = self.tablalibrosbuscar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"disponible", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"BUSCAR UN LIBRO", None))
        self.autorInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por Autor", None))
        self.buscarAutor.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
    # retranslateUi

