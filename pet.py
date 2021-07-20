from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from err3 import Ui_Error3
import mysql.connector
import sys

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor(buffered=True)

class Ui_Pet(QtWidgets.QDialog):

    def error(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Error3()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

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
        self.pushButton_3.clicked.connect(self.pet_input)
        self.pushButton_3.clicked.connect(lambda: Pet.close())


        self.lineEdit_6 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 80, 161, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.dateEdit_2 = QtWidgets.QDateEdit(Pet)
        self.dateEdit_2.setGeometry(QtCore.QRect(150, 170, 161, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))

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

        self.lineEdit_4 = QtWidgets.QLineEdit(Pet)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 20, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

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
        self.label_10.setGeometry(QtCore.QRect(20, 170, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(Pet)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.comboBox_2 = QtWidgets.QComboBox(Pet)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 200, 161, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        mycursor.execute("SELECT `customer_ID` FROM `customer`")
        records = mycursor.fetchall()

        for row in records:
            content = row[0]
            self.comboBox_2.addItem(content)

        self.retranslateUi(Pet)
        QtCore.QMetaObject.connectSlotsByName(Pet)

    def pet_input(self):
        self.id = self.lineEdit_4.text()
        self.name = self.lineEdit_5.text()
        self.animal = self.lineEdit_6.text()
        self.breed = self.lineEdit_7.text()
        self.gender = self.lineEdit_8.text()
        self.date = self.dateEdit_2.date().toPyDate()
        self.currentTxt = self.comboBox_2.currentText()

        id = self.id
        name = self.name
        animal = self.animal
        breed = self.breed
        gender = self.gender
        date = self.date
        text = self.currentTxt

        query = f"SELECT * FROM `pet` WHERE `pet_ID` = '{id}'"
        mycursor.execute(query)

        row = mycursor.fetchone()

        if row != None:
            self.error()
        else:
            mycursor.execute(
                "INSERT INTO `pet` (`pet_ID`, `pet_name`, `type_of_animal`, `breed`, `gender`, `birthday`, `customer_ID`) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (id, name, animal, breed, gender, date, text))
            db.commit()




    def retranslateUi(self, Pet):
        _translate = QtCore.QCoreApplication.translate
        Pet.setWindowTitle(_translate("Pet", "Pet ADD"))
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
    ui = Ui_Pet()
    ui.setupUi(Pet)
    Pet.show()
    sys.exit(app.exec_())
