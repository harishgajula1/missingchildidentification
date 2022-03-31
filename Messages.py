from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import re,os
import sys
from ChildInfo import Ui_ChildInfo
class Ui_Messages(object):

    def viewmsgs(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("SELECT *FROM messages")
            row = cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(row):
                self.tableWidget.insertRow(row_number)
                for col_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))


        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def viewpic(self):

        cid= self.lineEdit.text()

        if(cid=="" or cid == "null"):
            self.showMessageBox("Information", "Please fill out field")
        else:
            self.photo = QtWidgets.QDialog()
            self.ui = Ui_ChildInfo()
            self.ui.setupUi(self.photo)
            self.ui.view(cid)
            self.photo.show()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(581, 461)
        Dialog.setStyleSheet("background-color: rgb(16, 168, 170);")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 481, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 280, 171, 21))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Georgia\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 270, 171, 41))
        self.lineEdit.setStyleSheet("font: 12pt \"Georgia\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 330, 111, 31))
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 0);\n"
"font: 16pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.viewpic)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Messages"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Complaint ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "City"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "SearchBy"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Contact"))
        self.label.setText(_translate("Dialog", "Enter Complaint ID:"))
        self.pushButton.setText(_translate("Dialog", "View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
