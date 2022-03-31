from PyQt5 import QtCore, QtGui, QtWidgets
from Authority import Ui_Authority
from User import Ui_User
class Ui_Dialog(object):

    def authrtylogin(self, event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Authority(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def userlogin(self, event):
        try:
            self.usr = QtWidgets.QDialog()
            self.ui = Ui_User(self.usr)
            self.ui.setupUi(self.usr)
            self.usr.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 448)
        Dialog.setStyleSheet("background-color: rgb(99, 99, 74);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 40, 741, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 26pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.users = QtWidgets.QLabel(Dialog)
        self.users.setGeometry(QtCore.QRect(400, 150, 281, 171))
        self.users.setStyleSheet("image: url(../MissingChild/images/userss.png);")
        self.users.setText("")
        self.users.setObjectName("faculty")
        self.users.mousePressEvent=self.userlogin
        self.authrty = QtWidgets.QLabel(Dialog)
        self.authrty.setGeometry(QtCore.QRect(70, 160, 261, 141))
        self.authrty.setStyleSheet("image: url(../MissingChild/images/authrty.png);")
        self.authrty.setText("")
        self.authrty.setObjectName("admin")
        self.authrty.mousePressEvent=self.authrtylogin

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 320, 121, 31))
        self.label_2.setStyleSheet("font: 15pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 320, 121, 31))
        self.label_3.setStyleSheet("font: 15pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label.setText(_translate("Dialog", "Missing Child Identification System "))
        self.label_2.setText(_translate("Dialog", "Authority"))
        self.label_3.setText(_translate("Dialog", "Users"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
