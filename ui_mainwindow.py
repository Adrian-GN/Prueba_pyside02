# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(547, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 251, 345))
        self.Editorial_lineEdit = QLineEdit(self.groupBox)
        self.Editorial_lineEdit.setObjectName(u"Editorial_lineEdit")
        self.Editorial_lineEdit.setGeometry(QRect(90, 160, 141, 20))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 40, 30, 16))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 80, 31, 16))
        self.Agregar_Inicio_pushButton = QPushButton(self.groupBox)
        self.Agregar_Inicio_pushButton.setObjectName(u"Agregar_Inicio_pushButton")
        self.Agregar_Inicio_pushButton.setGeometry(QRect(10, 246, 211, 23))
        self.Titulo_lineEdit_2 = QLineEdit(self.groupBox)
        self.Titulo_lineEdit_2.setObjectName(u"Titulo_lineEdit_2")
        self.Titulo_lineEdit_2.setGeometry(QRect(90, 40, 141, 20))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 120, 49, 16))
        self.Agregar_Final_pushButton = QPushButton(self.groupBox)
        self.Agregar_Final_pushButton.setObjectName(u"Agregar_Final_pushButton")
        self.Agregar_Final_pushButton.setGeometry(QRect(10, 202, 211, 23))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 160, 42, 16))
        self.Autor_lineEdit = QLineEdit(self.groupBox)
        self.Autor_lineEdit.setObjectName(u"Autor_lineEdit")
        self.Autor_lineEdit.setGeometry(QRect(90, 80, 133, 20))
        self.Publicado_spinbox = QSpinBox(self.groupBox)
        self.Publicado_spinbox.setObjectName(u"Publicado_spinbox")
        self.Publicado_spinbox.setGeometry(QRect(90, 120, 61, 20))
        self.Publicado_spinbox.setMinimum(2000)
        self.Publicado_spinbox.setMaximum(2020)
        self.Mostrar_pushbutton = QPushButton(self.groupBox)
        self.Mostrar_pushbutton.setObjectName(u"Mostrar_pushbutton")
        self.Mostrar_pushbutton.setGeometry(QRect(10, 290, 211, 23))
        self.Salida = QPlainTextEdit(self.centralwidget)
        self.Salida.setObjectName(u"Salida")
        self.Salida.setGeometry(QRect(270, 10, 271, 341))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 547, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Libro:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Titulo:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.Agregar_Inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Publicado:", None))
        self.Agregar_Final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Editorial:", None))
        self.Mostrar_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi