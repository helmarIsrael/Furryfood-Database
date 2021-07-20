from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from err2 import Ui_Error2
import mysql.connector
import sys

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor(buffered=True)

class Ui_Customer(QtWidgets.QDialog):

    def error(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Error2()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def setupUi(self, Customer):
        Customer.setObjectName("Customer")
        Customer.resize(329, 192)
        Customer.setStyleSheet("background-color: rgb(255, 179, 71);")
        
        self.label = QtWidgets.QLabel(Customer)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_3 = QtWidgets.QLabel(Customer)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Customer)
        
        self.label_2.setGeometry(QtCore.QRect(10, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.lineEdit = QtWidgets.QLineEdit(Customer)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton = QtWidgets.QPushButton(Customer)
        self.pushButton.setGeometry(QtCore.QRect(80, 160, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.customer_input)
        self.pushButton.clicked.connect(lambda: Customer.close())
        
        self.pushButton_2 = QtWidgets.QPushButton(Customer)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 160, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: Customer.close())
        
        self.label_4 = QtWidgets.QLabel(Customer)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.dateEdit = QtWidgets.QDateEdit(Customer)
        self.dateEdit.setGeometry(QtCore.QRect(160, 120, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))

        self.lineEdit_2 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 60, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 90, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Customer)
        QtCore.QMetaObject.connectSlotsByName(Customer)

    def customer_input(self):
        self.code = self.lineEdit.text()
        self.name = self.lineEdit_2.text()
        self.number = self.lineEdit_4.text()
        self.date = self.dateEdit.date().toPyDate()

        code = self.code
        name = self.name
        number = self.number
        date = self.date

        query = f"SELECT * FROM `customer` WHERE `customer_ID` = '{code}'"
        mycursor.execute(query)

        row = mycursor.fetchone()

        if row != None:
            self.error()
        else:
            mycursor.execute("INSERT INTO `customer` (`customer_ID`, `customer_name`, `contact_number`, `birthday`) "
                             "VALUES (%s,%s,%s,%s)",
                             (code, name, number, date))
            db.commit()


    def retranslateUi(self, Customer):
        _translate = QtCore.QCoreApplication.translate
        Customer.setWindowTitle(_translate("Customer", "Customer ADD"))
        self.label.setText(_translate("Customer", "Customer ID:"))
        self.label_3.setText(_translate("Customer", "Customer Number:"))
        self.label_2.setText(_translate("Customer", "Customer Name:"))
        self.pushButton.setText(_translate("Customer", "OK"))
        self.pushButton_2.setText(_translate("Customer", "Cancel"))
        self.label_4.setText(_translate("Customer", "Customer Birthday:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Customer = QtWidgets.QDialog()
    ui = Ui_Customer()
    ui.setupUi(Customer)
    Customer.show()
    sys.exit(app.exec_())
