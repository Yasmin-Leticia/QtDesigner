# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reprodutor_musica.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(260, 110, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setStyleSheet("background-color: #fff;")
        self.pushButton_play.setObjectName("pushButton_play")
        self.pushButton_parar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_parar.setGeometry(QtCore.QRect(260, 240, 75, 23))
        self.pushButton_parar.setStyleSheet("background-color: #fff;")
        self.pushButton_parar.setObjectName("pushButton_parar")
        self.pushButton_pausar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pausar.setGeometry(QtCore.QRect(430, 240, 75, 23))
        self.pushButton_pausar.setStyleSheet("background-color: #fff;")
        self.pushButton_pausar.setObjectName("pushButton_pausar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.pushButton_parar.setText(_translate("MainWindow", "Parar"))
        self.pushButton_pausar.setText(_translate("MainWindow", "pausar"))
