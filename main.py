from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlQueryModel
from appointment import Ui_Appointment
from customer import Ui_Customer
from pet import Ui_Pet
from AU import Ui_AU
from CU import Ui_CU
from PU import Ui_PU
from AD import Ui_AD
from CD import Ui_CD
from PD import Ui_PD
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor()

class Ui_FurryFoodDatabase(object):

    def add_appointment(self):
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Appointment()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

    def add_customer(self):
        self.dialog2 = QtWidgets.QDialog()
        self.ui2 = Ui_Customer()
        self.ui2.setupUi(self.dialog2)
        self.dialog2.show()

    def add_pet(self):
        self.dialog3 = QtWidgets.QDialog()
        self.ui3 = Ui_Pet()
        self.ui3.setupUi(self.dialog3)
        self.dialog3.show()

    def update_app(self):
        self.dialog4 = QtWidgets.QDialog()
        self.ui4 = Ui_AU()
        self.ui4.setupUi(self.dialog4)
        self.dialog4.show()

    def update_customer(self):
        self.dialog5 = QtWidgets.QDialog()
        self.ui5 = Ui_CU()
        self.ui5.setupUi(self.dialog5)
        self.dialog5.show()

    def update_pet(self):
        self.dialog6 = QtWidgets.QDialog()
        self.ui6 = Ui_PU()
        self.ui6.setupUi(self.dialog6)
        self.dialog6.show()

    def delete_app(self):
        self.dialog7 = QtWidgets.QDialog()
        self.ui7 = Ui_AD()
        self.ui7.setupUi(self.dialog7)
        self.dialog7.show()

    def delete_customer(self):
        self.dialog8 = QtWidgets.QDialog()
        self.ui8 = Ui_CD()
        self.ui8.setupUi(self.dialog8)
        self.dialog8.show()

    def delete_pet(self):
        self.dialog9 = QtWidgets.QDialog()
        self.ui9 = Ui_PD()
        self.ui9.setupUi(self.dialog9)
        self.dialog9.show()

    def setupUi(self, FurryFoodDatabase):
        FurryFoodDatabase.setObjectName("FurryFoodDatabase")
        FurryFoodDatabase.resize(691, 463)
        FurryFoodDatabase.setStyleSheet("background-color: rgb(255, 179, 71);")

        self.centralwidget = QtWidgets.QWidget(FurryFoodDatabase)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.clicked.connect(self.states_of_buttons)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 150, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 221, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.clicked.connect(self.states_of_buttons2)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 180, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.clicked.connect(self.states_of_buttons3)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 90, 481, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")

        self.table = QSqlQueryModel()

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 320, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 238, 210);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 380, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 238, 210);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 350, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 238, 210);")
        self.pushButton_6.setObjectName("pushButton_6")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 20, 121, 71))
        self.widget.setObjectName("widget")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, -8, 121, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../2.1.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        FurryFoodDatabase.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FurryFoodDatabase)
        self.statusbar.setObjectName("statusbar")
        FurryFoodDatabase.setStatusBar(self.statusbar)

        self.retranslateUi(FurryFoodDatabase)
        QtCore.QMetaObject.connectSlotsByName(FurryFoodDatabase)

    def states_of_buttons(self):
        if self.pushButton.isChecked():
            try:
                self.clear_table()
                self.pushButton_4.disconnect()
                self.pushButton_6.disconnect()
                self.pushButton_5.disconnect()
                self.pushButton_2.setChecked(False)
                self.pushButton_3.setChecked(False)
                self.pushButton_4.clicked.connect(self.add_appointment)
                self.pushButton_6.clicked.connect(self.update_app)
                self.pushButton_5.clicked.connect(self.delete_app)
                self.tableWidget.setRowCount(49)
                self.tableWidget.setColumnCount(4)
                print("a")
                mycursor.execute("SELECT * FROM `appointment`")

                result = mycursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                db.commit()
            except:
                self.clear_table()
                self.pushButton_2.setChecked(False)
                self.pushButton_3.setChecked(False)
                self.pushButton_4.clicked.connect(self.add_appointment)
                self.pushButton_6.clicked.connect(self.update_app)
                self.pushButton_5.clicked.connect(self.delete_app)
                self.tableWidget.setRowCount(49)
                self.tableWidget.setColumnCount(4)
                print("b")
                mycursor.execute("SELECT * FROM `appointment`")

                result = mycursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                db.commit()

        else:
            self.pushButton_4.disconnect()
            self.pushButton_6.disconnect()
            self.pushButton_5.disconnect()
            self.clear_table()

    def states_of_buttons2(self):
        if self.pushButton_2.isChecked():
            try:
                self.clear_table()
                self.pushButton_4.disconnect()
                self.pushButton_6.disconnect()
                self.pushButton_5.disconnect()
                self.pushButton.setChecked(False)
                self.pushButton_3.setChecked(False)
                self.pushButton_4.clicked.connect(self.add_customer)
                self.pushButton_6.clicked.connect(self.update_customer)
                self.pushButton_5.clicked.connect(self.delete_customer)
                self.tableWidget.setRowCount(49)
                self.tableWidget.setColumnCount(4)
                mycursor.execute("SELECT * FROM `Customer`")

                result = mycursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                db.commit()
            except:
                self.clear_table()
                self.pushButton.setChecked(False)
                self.pushButton_3.setChecked(False)
                self.pushButton_4.clicked.connect(self.add_customer)
                self.pushButton_6.clicked.connect(self.update_customer)
                self.pushButton_5.clicked.connect(self.delete_customer)
                self.tableWidget.setRowCount(49)
                self.tableWidget.setColumnCount(4)
                mycursor.execute("SELECT * FROM `Customer`")

                result = mycursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                db.commit()
        else:
            self.pushButton_4.disconnect()
            self.pushButton_6.disconnect()
            self.pushButton_5.disconnect()
            self.clear_table()

    def states_of_buttons3(self):
        if self.pushButton_3.isChecked():
            try:
                self.clear_table()
                self.pushButton_4.disconnect()
                self.pushButton_6.disconnect()
                self.pushButton_5.disconnect()
                self.pushButton.setChecked(False)
                self.pushButton_2.setChecked(False)
                self.pushButton_4.clicked.connect(self.add_pet)
                self.pushButton_6.clicked.connect(self.update_pet)
                self.pushButton_5.clicked.connect(self.delete_pet)
                self.tableWidget.setRowCount(49)
                self.tableWidget.setColumnCount(7)
                mycursor.execute("SELECT * FROM `Pet`")

                result = mycursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                db.commit()
            except:
                self.clear_table()
                self.pushButton.setChecked(False)
                self.pushButton_2.setChecked(False)
                self.pushButton_4.clicked.connect(self.add_pet)
                self.pushButton_6.clicked.connect(self.update_pet)
                self.pushButton_5.clicked.connect(self.delete_pet)
                self.tableWidget.setRowCount(49)
                self.tableWidget.setColumnCount(7)
                self.pushButton_4.clicked.connect(self.add_pet)
                mycursor.execute("SELECT * FROM `Pet`")

                result = mycursor.fetchall()
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                db.commit()
        else:
            self.pushButton_4.disconnect()
            self.pushButton_6.disconnect()
            self.pushButton_5.disconnect()
            self.clear_table()

    def clear_table(self):
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

    def retranslateUi(self, FurryFoodDatabase):
        _translate = QtCore.QCoreApplication.translate
        FurryFoodDatabase.setWindowTitle(_translate("FurryFoodDatabase", "FurryFood Database"))
        self.label.setText(_translate("FurryFoodDatabase", "FurryFood "))
        self.pushButton.setText(_translate("FurryFoodDatabase", "Appointments"))
        self.pushButton_2.setText(_translate("FurryFoodDatabase", "Customers"))
        self.pushButton_3.setText(_translate("FurryFoodDatabase", "Pets"))
        self.pushButton_4.setText(_translate("FurryFoodDatabase", "Add"))
        self.pushButton_5.setText(_translate("FurryFoodDatabase", "Delete"))
        self.pushButton_6.setText(_translate("FurryFoodDatabase", "Update"))
        self.label_2.setText(_translate("FurryFoodDatabase", " Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FurryFoodDatabase = QtWidgets.QMainWindow()
    ui = Ui_FurryFoodDatabase()
    ui.setupUi(FurryFoodDatabase)
    FurryFoodDatabase.show()
    sys.exit(app.exec_())
