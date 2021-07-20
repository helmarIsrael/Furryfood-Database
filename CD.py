from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor()

class Ui_CD(object):
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

        self.pushButton = QtWidgets.QPushButton(Customer)
        self.pushButton.setGeometry(QtCore.QRect(80, 160, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.proceed)
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
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")

        self.lineEdit_2 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 60, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_4 = QtWidgets.QLineEdit(Customer)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 90, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.comboBox = QtWidgets.QComboBox(Customer)
        self.comboBox.setGeometry(QtCore.QRect(160, 30, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.check_customer()
        self.update()
        self.comboBox.currentIndexChanged.connect(self.update)

        self.retranslateUi(Customer)
        QtCore.QMetaObject.connectSlotsByName(Customer)

    def check_customer(self):
        mycursor.execute("SELECT `customer_ID` FROM `customer`")
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox.addItem(content)

    def check_status(self):
        self.customer_ID = self.comboBox.currentText()
        query = f"SELECT `customer_name` FROM `customer` WHERE `customer_ID` = '{self.customer_ID}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_2.setText(status)

    def check_number(self):
        self.customer_ID = self.comboBox.currentText()
        query = f"SELECT `contact_number` FROM `customer` WHERE `customer_ID` = '{self.customer_ID}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = str(status[0])
        self.lineEdit_4.setText(status)

    def check_date(self):
        self.customer_ID = self.comboBox.currentText()
        query = f"SELECT DATE(`birthday`) FROM `customer` WHERE `customer_ID` = '{self.customer_ID}'"
        mycursor.execute(query)
        dates = mycursor.fetchone()
        new_date = dates[0]
        self.dateEdit.setDate(new_date)

    def update(self):
        self.check_status()
        self.check_number()
        self.check_date()

    def proceed(self):
        self.code = self.comboBox.currentText()

        query2 = f"DELETE FROM `customer` WHERE `customer_ID` = '{self.code}'"
        mycursor.execute(query2)
        db.commit()

    def retranslateUi(self, Customer):
        _translate = QtCore.QCoreApplication.translate
        Customer.setWindowTitle(_translate("Customer", "Customer DELETE"))
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
    ui = Ui_CD()
    ui.setupUi(Customer)
    Customer.show()
    sys.exit(app.exec_())
