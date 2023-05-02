import sys
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QLabel, QButtonGroup, QMainWindow
import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'ENGINE OPTIONS'

        self.label = QLabel('Please only choose one option: ', self)



        checkbox = QCheckBox('Play Against the Chess AI as White', self)
        checkbox.stateChanged.connect(self.change_state)
        checkbox.move(10, 40)
        checkbox2 = QCheckBox('Play Against the Chess AI as Black', self)
        checkbox2.stateChanged.connect(self.change_secondstate)
        checkbox2.move(10, 90)
        checkbox3 = QCheckBox('Enable Engine Analysis mode', self)
        checkbox3.stateChanged.connect(self.change_thirdstate)
        checkbox3.move(10, 140)
        checkbox4 = QCheckBox('Disable Engine Analysis mode: ', self)
        checkbox4.stateChanged.connect(self.change_fourthstate)
        checkbox4.move(10, 190)


        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 240
        self.initUI()

    def change_state(self, state):
        if state == Qt.Checked:
            playerOne = False
            playerTwo = True
        else:
            playerOne = True
            playerTwo = True

    def change_secondstate(self, state):
        if state == Qt.Checked:
            playerTwo = False
            playerOne = True
        else:
            playerTwo = True
            playerOne = True

    def change_thirdstate(self, state):
        if state == Qt.Checked:
            playerTwo = True
            playerOne = True
        else:
            playerOne = True
            playerTwo = True

    def change_fourthstate(self, state):
        if state == Qt.Checked:
            playerTwo = True
            playerOne = True
        else:
            playerOne = True
            playerTwo = True

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.move(600, 325)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())