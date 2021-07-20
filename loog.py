from main import *
from invalid import *
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="furry"
)
mycursor = db.cursor(buffered=True)

class Ui_MainWindow(object):
    def main_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FurryFoodDatabase()
        self.ui.setupUi(self.window)
        self.window.show()

    def invalid(self):
        self.dialog2 = QtWidgets.QDialog()
        self.ui = Ui_Invalid()
        self.ui.setupUi(self.dialog2)
        self.dialog2.show()

    def setupUi(self, Log):
        Log.setObjectName("Log")
        Log.resize(338, 218)
        Log.setStyleSheet("background-color: rgb(255, 179, 71);")

        self.centralwidget = QtWidgets.QWidget(Log)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 61, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 51, 20))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 130, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.log)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 130, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 223, 158);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda :Log.close())

        Log.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Log)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 21))
        self.menubar.setObjectName("menubar")
        Log.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Log)
        self.statusbar.setObjectName("statusbar")
        Log.setStatusBar(self.statusbar)

        self.retranslateUi(Log)
        QtCore.QMetaObject.connectSlotsByName(Log)


    def log(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == '' or password == '':
            self.invalid()

        query = f"SELECT * FROM `user` WHERE `username` = '{username}' AND `password` = '{password}'"
        mycursor.execute(query)

        row = mycursor.fetchone()


        if row != None:
            self.main_menu()
            MainWindow.close()
        else:
            self.invalid()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Log", "Log In"))
        self.label.setText(_translate("Log", "Username:"))
        self.label_2.setText(_translate("Log", "Password:"))
        self.pushButton.setText(_translate("Log", "OK"))
        self.pushButton_2.setText(_translate("Log", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
