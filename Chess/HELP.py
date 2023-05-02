import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, QLabel, QGridLayout
import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Explanation of Features'
        self.left = 10
        self.top = 10
        self.width = 200
        self.height = 200
        self.initUI()

        self.setLayout(qtw.QVBoxLayout())
        my_label = qtw.QLabel("The is the Chess Board where you can complete your chess analysis or play against the Chess AI.")
        label2 = qtw.QLabel("The Notation log is where your moves will be recorded and you can perform your own analysis.")
        label3 = qtw.QLabel("The SAVE button will save the current game and recordings in the Notation log.")
        label4 = qtw.QLabel("The NEW button will open a new Board and Notation log, remember to save your previous one.")
        label5 = qtw.QLabel("The ENGINE button allows you to modify the actions of the Chess Engine or Chess AI.")
        label6 = qtw.QLabel("The COLOUR THEMES button allows you to modify the colours of the Chess Board.")
        label7 = qtw.QLabel("Those are all the current functioning features of ChessBasics")

        self.layout().addWidget(my_label)
        self.layout().addWidget(label2)
        self.layout().addWidget(label3)
        self.layout().addWidget(label4)
        self.layout().addWidget(label5)
        self.layout().addWidget(label6)
        self.layout().addWidget(label7)


        self.move(450,325)

        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

