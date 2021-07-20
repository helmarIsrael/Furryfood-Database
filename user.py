from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class table(QMainWindow):
    def __init__(self):
        super(table, self).__init__()
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle("SSIS v2")
        self.initUI()

    def initUI(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Proceed")
        self.b1.move(75, 110)


def new():
    app = QApplication(sys.argv)
    win = table()

    win.show()
    sys.exit(app.exec_())


new()