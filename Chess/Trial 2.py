import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIcon



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 300
        self.initUI()

        self.setLayout(qtw.QVBoxLayout())
        my_label = qtw.QLabel("name")
        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name field")
        my_entry.setText(" ")
        self.layout().addWidget(my_entry)

        another1 = qtw.QLabel("rating of 1:")
        self.layout().addWidget(another1)

        rating1 = qtw.QLineEdit()
        rating1.setObjectName("Rating of player 1: ")
        rating1.setText(" ")
        self.layout().addWidget(rating1)

        another2 = qtw.QLabel("rating of 2: ")
        self.layout().addWidget(another2)

        rating2 = qtw.QLineEdit()
        rating2.setObjectName("Rating of player 2: ")
        rating2.setText(" ")
        self.layout().addWidget(rating2)




        my_button = qtw.QPushButton("Confirm", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        #entry_rating1 = qtw.QPushButton("")

        def press_it():
            my_label.setText(f'player one: {my_entry.text()} vs player 2')
            my_entry.setText("")

        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    another1 = qtw.QLabel("rating of 1:")
    self.layout().addWidget(another1)

    rating1 = qtw.QLineEdit()
    rating1.setObjectName("Rating of player 1: ")
    rating1.setText(" ")
    self.layout().addWidget(rating1)

    another2 = qtw.QLabel("rating of 2: ")
    self.layout().addWidget(another2)

    rating2 = qtw.QLineEdit()
    rating2.setObjectName("Rating of player 2: ")
    rating2.setText(" ")
    self.layout().addWidget(rating2)