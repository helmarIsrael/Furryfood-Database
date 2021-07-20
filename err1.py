from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error1(object):
    def setupUi(self, Error1):
        Error1.setObjectName("Error1")
        Error1.resize(165, 90)
        Error1.setStyleSheet("background-color: rgb(255, 161, 148);\n"
"background-color: rgb(199, 199, 199);")
        self.label = QtWidgets.QLabel(Error1)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Error1)
        self.pushButton.setGeometry(QtCore.QRect(45, 40, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: Error1.close())

        self.retranslateUi(Error1)
        QtCore.QMetaObject.connectSlotsByName(Error1)

    def retranslateUi(self, Error1):
        _translate = QtCore.QCoreApplication.translate
        Error1.setWindowTitle(_translate("Error1", "Invalid"))
        self.label.setText(_translate("Error1", "Customer ID already exist!"))
        self.pushButton.setText(_translate("Error1", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error1 = QtWidgets.QDialog()
    ui = Ui_Error1()
    ui.setupUi(Error1)
    Error1.show()
    sys.exit(app.exec_())
