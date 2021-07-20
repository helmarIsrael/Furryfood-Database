from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from err1 import Ui_Error1
import mysql.connector
import sys

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor(buffered=True)

class Ui_Appointment(QtWidgets.QDialog):
    
    def error(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Error1()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
    
    def setupUi(self, Appointment):
        Appointment.setObjectName("Appointment")
        Appointment.resize(333, 194)
        Appointment.setStyleSheet("background-color: rgb(255, 179, 71);")

        self.lineEdit = QtWidgets.QLineEdit(Appointment)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(Appointment)
        self.label.setGeometry(QtCore.QRect(10, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Appointment)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Appointment)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(Appointment)
        self.pushButton.setGeometry(QtCore.QRect(80, 160, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.appointment_input)
        self.pushButton.clicked.connect(lambda: Appointment.close())
        
        self.pushButton_2 = QtWidgets.QPushButton(Appointment)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 160, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: Appointment.close())

        self.comboBox = QtWidgets.QComboBox(Appointment)
        self.comboBox.setGeometry(QtCore.QRect(150, 120, 161, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        mycursor.execute("SELECT `customer_ID` FROM `customer`")
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox.addItem(content)

        self.label_4 = QtWidgets.QLabel(Appointment)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_3 = QtWidgets.QLineEdit(Appointment)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 90, 161, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.dateEdit = QtWidgets.QDateEdit(Appointment)
        self.dateEdit.setGeometry(QtCore.QRect(150, 60, 161, 22))
        self.dateEdit.setAutoFillBackground(False)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))

        self.retranslateUi(Appointment)
        QtCore.QMetaObject.connectSlotsByName(Appointment)

    def appointment_input(self):
        self.code = self.lineEdit.text()
        self.date = self.dateEdit.date().toPyDate()
        self.status = self.lineEdit_3.text()
        self.currentTxt = self.comboBox.currentText()

        code = self.code
        date = self.date
        status = self.status
        text = self.currentTxt

        query = f"SELECT * FROM `appointment` WHERE `appointment_ID` = '{code}'"
        mycursor.execute(query)

        row = mycursor.fetchone()

        if row != None:
            self.error()
        else:
            mycursor.execute(
                "INSERT INTO `appointment` (`appointment_ID`, `appointment_date`, `appointment_status`, `customer_ID`) "
                "VALUES (%s,%s,%s,%s)",
                (code, date, status, text))
            db.commit()

    def retranslateUi(self, Appointment):
        _translate = QtCore.QCoreApplication.translate
        Appointment.setWindowTitle(_translate("Appointment", "Appointment ADD"))
        self.label.setText(_translate("Appointment", "Appointment Code:"))
        self.label_2.setText(_translate("Appointment", "Appointment Date:"))
        self.label_3.setText(_translate("Appointment", "Customer ID:"))
        self.pushButton.setText(_translate("Appointment", "OK"))
        self.pushButton_2.setText(_translate("Appointment", "Cancel"))
        self.label_4.setText(_translate("Appointment", "Appointment Status:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Appointment = QtWidgets.QDialog()
    ui = Ui_Appointment()
    ui.setupUi(Appointment)
    Appointment.show()
    sys.exit(app.exec_())
