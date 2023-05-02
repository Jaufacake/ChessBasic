# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'MAIN_SCREEN.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from SAVE_SCREEN import *
from COLOUR_THEMES import *
from PIECES_THEMES2 import *
from ENGINE_SCREEN import *
import pygame as p
import sys
from Chess import ChessEngine
from ChessMain import *
from ChessEngine import *
import os

running = True

class Ui_MainWindow(object):
    def ok(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SAVE_SCREEN1()
        self.ui.setup(self.window)
        self.window.show()

    def ok2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PIECES_THEME1()
        self.ui.setup(self.window)
        self.window.show()

    def ok3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_COLOUR_THEMES2()
        self.ui.setup(self.window)
        self.window.show()

    def ok4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setup(self.window)
        self.window.show()

    def ok5(self):
        print("CLICKED")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 708)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 101, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ok)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 10, 101, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 10, 101, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 10, 171, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 10, 141, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.ok2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(500, 10, 141, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.ok3)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(380, 10, 101, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.ok4)

        #self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_8.setGeometry(QtCore.QRect(10, 105, 615, 555))
        #self.pushButton_8.setObjectName("pushButton_8")
        #self.pushButton_8.main()
        #self.pushButton_8.clicked.connect(self.ok5)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(633, 98, 371, 311))
        self.tabWidget.resize(370, 560)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("NOTATION")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("GAME REPORT")
        self.tabWidget.addTab(self.tab_2, "")

        #self.widget = QtWidgets.QWidget(self.centralwidget)
        #self.widget.setGeometry(QtCore.QRect(27, 107, 501, 421))
        #self.widget.setFixedSize(600, 550)
        #self.widget.setObjectName("Widget")


        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1010, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "Chess Program"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "NOTATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "GAME REPORT"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SAVE"))
        self.pushButton_2.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_3.setText(_translate("MainWindow", "NEW GAME"))
        self.pushButton_4.setText(_translate("MainWindow", "VISUALISATION GAME"))
        self.pushButton_5.setText(_translate("MainWindow", "PIECES THEMES"))
        self.pushButton_6.setText(_translate("MainWindow", "COLOUR THEMES"))
        self.pushButton_7.setText(_translate("MainWindow", "ENGINE"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a new file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))

        _translate = QtCore.QCoreApplication.translate


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main()
    #if sys.exit(app.exec_()):
       # main.QUIT
    #sys.exit(app.exec_())





