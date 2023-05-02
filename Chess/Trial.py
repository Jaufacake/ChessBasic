import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("lets try this again")

        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("save screen baby")
        my_label.setFont(qtg.QFont('Helvetica', 20))

        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name field")
        my_entry.setText(" ")
        self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton("Confirm", clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        self.show()

        def press_it():
            my_label.setText(f'player one: {my_entry.text()} vs player 2')
            my_entry.setText("")




app = qtw.QApplication([])
mw = MainWindow()

app.exec_()