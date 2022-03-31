from PyQt5 import QtCore, QtGui, QtWidgets
import re
import sys
from UserUploadPhoto import Ui_UserUploadPhoto
from UserSearch import Ui_UserSearch
class Ui_UserHome(object):

    def __init__(self, Dialog, unm):
        self.dialog = Dialog
        self.unm = unm

    def upload_photo(self):

        try:
            self.photo = QtWidgets.QDialog()
            self.ui = Ui_UserUploadPhoto(self.photo, self.unm)
            self.ui.setupUi(self.photo)
            self.photo.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def search_photo(self):

        try:
            self.photo = QtWidgets.QDialog()
            self.ui = Ui_UserSearch(self.photo,self.unm)
            self.ui.setupUi(self.photo)
            self.photo.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 445)
        Dialog.setStyleSheet("background-color: rgb(155, 200, 70);")
        self.addstdnt = QtWidgets.QLabel(Dialog)
        self.addstdnt.setGeometry(QtCore.QRect(-140, -60, 831, 561))
        self.addstdnt.setStyleSheet("image: url(../MissingChild/images/bg3.jpg);")
        self.addstdnt.setText("")
        self.addstdnt.setObjectName("addstdnt")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 100, 201, 41))
        self.pushButton.setStyleSheet("font: 14pt \"Georgia\";\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.upload_photo)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 220, 201, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"Georgia\";\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.search_photo)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "User Home"))
        self.pushButton.setText(_translate("Dialog", "Upload Photo"))
        self.pushButton_2.setText(_translate("Dialog", "Search"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_UserHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
