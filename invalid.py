from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Invalid(object):
    def setupUi(self, Invalid):
        Invalid.setObjectName("Invalid")
        Invalid.resize(336, 130)
        Invalid.setStyleSheet("background-color: rgb(255, 179, 71)")
        self.label = QtWidgets.QLabel(Invalid)
        self.label.setGeometry(QtCore.QRect(20, 40, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Invalid)
        self.pushButton.setGeometry(QtCore.QRect(130, 80, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda :Invalid.close())

        self.retranslateUi(Invalid)
        QtCore.QMetaObject.connectSlotsByName(Invalid)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Invalid", "Warning"))
        self.label.setText(_translate("Invalid", "Invalid Username or Password!"))
        self.pushButton.setText(_translate("Invalid", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Invalid()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
