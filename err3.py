from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error3(object):
    def setupUi(self, Error3):
        Error3.setObjectName("Error3")
        Error3.resize(156, 88)
        Error3.setStyleSheet("background-color: rgb(255, 161, 148);\n"
"background-color: rgb(199, 199, 199);")
        self.pushButton_2 = QtWidgets.QPushButton(Error3)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(Error3.close)
        self.label_2 = QtWidgets.QLabel(Error3)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Error3)
        QtCore.QMetaObject.connectSlotsByName(Error3)

    def retranslateUi(self, Error2):
        _translate = QtCore.QCoreApplication.translate
        Error2.setWindowTitle(_translate("Error3", "Invalid"))
        self.pushButton_2.setText(_translate("Error3", "OK"))
        self.label_2.setText(_translate("Error3", "Pet ID already exist!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error3 = QtWidgets.QDialog()
    ui = Ui_Error3()
    ui.setupUi(Error3)
    Error3.show()
    sys.exit(app.exec_())
