from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor()

class Ui_PU(object):
    def setupUi(self, Pet):
        Pet.setObjectName("Pet")
        Pet.resize(334, 282)
        Pet.setStyleSheet("background-color: rgb(255, 179, 71);")

        self.pushButton_4 = QtWidgets.QPushButton(Pet)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 250, 75, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: Pet.close())

        self.pushButton_3 = QtWidgets.QPushButton(Pet)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 250, 75, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.proceed)
        self.pushButton_3.clicked.connect(lambda: Pet.close())

        self.lineEdit_6 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 80, 161, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.dateEdit = QtWidgets.QDateEdit(Pet)
        self.dateEdit.setGeometry(QtCore.QRect(150, 170, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")

        self.label_6 = QtWidgets.QLabel(Pet)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Pet)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_5 = QtWidgets.QLabel(Pet)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEdit_5 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 50, 161, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_8 = QtWidgets.QLabel(Pet)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.lineEdit_7 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 110, 161, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_8 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 140, 161, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.label_9 = QtWidgets.QLabel(Pet)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Pet)
        self.label_10.setGeometry(QtCore.QRect(20, 170, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(Pet)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.comboBox = QtWidgets.QComboBox(Pet)
        self.comboBox.setGeometry(QtCore.QRect(150, 20, 161, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(Pet)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 200, 161, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Pet)
        QtCore.QMetaObject.connectSlotsByName(Pet)

        self.check_petID()
        self.update()
        self.comboBox.currentIndexChanged.connect(self.update)

    def check_petID(self):
        mycursor.execute("SELECT `pet_ID` FROM `pet`")
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox.addItem(content)

    def check_pet_name(self):
        self.pet_ID = self.comboBox.currentText()
        query = f"SELECT `pet_name` FROM `pet` WHERE `pet_ID` = '{self.pet_ID}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_5.setText(status)

    def check_type(self):
        self.pet_ID = self.comboBox.currentText()
        query = f"SELECT `type_of_animal` FROM `pet` WHERE `pet_ID` = '{self.pet_ID}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_6.setText(status)

    def check_breed(self):
        self.pet_ID = self.comboBox.currentText()
        query = f"SELECT `breed` FROM `pet` WHERE `pet_ID` = '{self.pet_ID}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_7.setText(status)

    def check_gender(self):
        self.pet_ID = self.comboBox.currentText()
        query = f"SELECT `gender` FROM `pet` WHERE `pet_ID` = '{self.pet_ID}'"
        mycursor.execute(query)
        status = mycursor.fetchone()
        status = status[0]
        self.lineEdit_8.setText(status)

    def check_date(self):
        self.pet_ID = self.comboBox.currentText()
        query = f"SELECT DATE(`birthday`) FROM `pet` WHERE `pet_ID` = '{self.pet_ID}'"
        mycursor.execute(query)
        dates = mycursor.fetchone()
        new_date = dates[0]
        self.dateEdit.setDate(new_date)

    def check_customer(self):
        self.comboBox_2.clear()
        mycursor.execute("SELECT `customer_ID` FROM `customer`")
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox_2.addItem(content)

        self.appointment_ID = self.comboBox_2.currentText()
        query = f"SELECT `customer_ID` FROM `pet` WHERE `pet_ID` = '{self.pet_ID}'"
        mycursor.execute(query)
        customer = mycursor.fetchone()
        customer = customer[0]
        a = 0
        while True:
            self.comboBox_2.setCurrentIndex(a)
            if self.comboBox_2.currentText() == customer:
                self.comboBox_2.setItemText(a, customer)
                a = 0
                break
            else:
                a += 1
                if a > self.comboBox_2.count():
                    break

    def update(self):
        self.check_pet_name()
        self.check_type()
        self.check_breed()
        self.check_gender()
        self.check_date()
        self.check_customer()

    def proceed(self):
        self.code = self.comboBox.currentText()
        self.name = self.lineEdit_5.text()
        self.type = self.lineEdit_6.text()
        self.breed = self.lineEdit_7.text()
        self.gender = self.lineEdit_8.text()
        self.date = self.dateEdit.date().toPyDate()
        self.customer = self.comboBox_2.currentText()

        code = self.code
        name = self.name
        type = self.type
        breed = self.breed
        gender = self.gender
        date = self.date
        customer = self.customer

        query2 = f"UPDATE `pet` SET `pet_ID` = '{code}', `pet_name` = '{name}', `type_of_animal` = '{type}', `breed` = '{breed}', `gender` = '{gender}', `birthday` = '{date}', `customer_ID` = '{customer}' WHERE `pet_ID` = '{code}'"
        mycursor.execute(query2)
        db.commit()

    def retranslateUi(self, Pet):
        _translate = QtCore.QCoreApplication.translate
        Pet.setWindowTitle(_translate("Pet", "Pet UPDATE"))
        self.pushButton_4.setText(_translate("Pet", "Cancel"))
        self.pushButton_3.setText(_translate("Pet", "OK"))
        self.label_6.setText(_translate("Pet", "Pet ID:"))
        self.label_7.setText(_translate("Pet", "Type of Animal:"))
        self.label_5.setText(_translate("Pet", "Breed:"))
        self.label_8.setText(_translate("Pet", "Pet Name:"))
        self.label_9.setText(_translate("Pet", "Gender:"))
        self.label_10.setText(_translate("Pet", "Birthday:"))
        self.label_11.setText(_translate("Pet", "Customer ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pet = QtWidgets.QDialog()
    ui = Ui_PU()
    ui.setupUi(Pet)
    Pet.show()
    sys.exit(app.exec_())
