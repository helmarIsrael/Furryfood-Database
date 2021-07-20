from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor()

class Ui_AD(object):
    def setupUi(self, Appointment):
        Appointment.setObjectName("Appointment")
        Appointment.resize(333, 194)
        Appointment.setStyleSheet("background-color: rgb(255, 179, 71);")

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
        self.pushButton.clicked.connect(self.proceed)
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

        self.comboBox_2 = QtWidgets.QComboBox(Appointment)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 30, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")


        self.retranslateUi(Appointment)
        QtCore.QMetaObject.connectSlotsByName(Appointment)

        self.check_appointments()
        self.update()
        self.comboBox_2.currentIndexChanged.connect(self.update)

    def check_appointments(self):
        mycursor.execute("SELECT `appointment_ID` FROM `appointment`")
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox_2.addItem(content)

    def check_date(self):
        self.appointment_ID = self.comboBox_2.currentText()
        query = f"SELECT DATE(`appointment_date`) FROM `appointment` WHERE `appointment_ID` = '{self.appointment_ID}'"
        mycursor.execute(query)
        dates = mycursor.fetchone()
        new_date = dates[0]
        self.dateEdit.setDate(new_date)

    def check_status(self):
        self.appointment_ID = self.comboBox_2.currentText()
        query = f"SELECT `appointment_status` FROM `appointment` WHERE `appointment_ID` = '{self.appointment_ID}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_3.setText(status)

    def check_customer(self):
        self.comboBox.clear()
        mycursor.execute("SELECT `customer_ID` FROM `customer`")
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox.addItem(content)

        self.appointment_ID = self.comboBox_2.currentText()
        query = f"SELECT `customer_ID` FROM `appointment` WHERE `appointment_ID` = '{self.appointment_ID}'"
        mycursor.execute(query)
        customer = mycursor.fetchone()
        customer = customer[0]
        a = 0
        while True:
            self.comboBox.setCurrentIndex(a)
            if self.comboBox.currentText() == customer:
                self.comboBox.setItemText(a, customer)
                a = 0
                break
            else:
                a += 1
                if a > self.comboBox.count():
                    break

    def update(self):
        self.check_date()
        self.check_status()
        self.check_customer()

    def proceed(self):
        self.code = self.comboBox_2.currentText()

        query2 = f"DELETE from `appointment` WHERE `appointment_ID` = '{self.code}'"
        mycursor.execute(query2)
        db.commit()

    def retranslateUi(self, Appointment):
        _translate = QtCore.QCoreApplication.translate
        Appointment.setWindowTitle(_translate("Appointment", "Appointment DELETE"))
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
    ui = Ui_AD()
    ui.setupUi(Appointment)
    Appointment.show()
    sys.exit(app.exec_())
