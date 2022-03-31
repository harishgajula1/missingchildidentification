from PyQt5 import QtCore, QtGui, QtWidgets
import re
import sys
from UploadPhoto import Ui_UploadPhoto
from Search import Ui_Search
from Messages import Ui_Messages
class Ui_AuthorityHome(object):

    def __init__(self, Dialog,unm):
        self.dialog = Dialog
        self.unm=unm

    def upload_photo(self):

        try:
            self.photo = QtWidgets.QDialog()
            self.ui = Ui_UploadPhoto(self.photo,self.unm)
            self.ui.setupUi(self.photo)
            self.photo.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


    def search_photo(self):

        try:
            self.photo = QtWidgets.QDialog()
            self.ui = Ui_Search(self.photo,self.unm)
            self.ui.setupUi(self.photo)
            self.photo.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def messages(self):

        try:
            self.msg = QtWidgets.QDialog()
            self.ui = Ui_Messages()
            self.ui.setupUi(self.msg)
            self.ui.viewmsgs()
            self.msg.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(548, 484)
        Dialog.setStyleSheet("background-color: rgb(155, 200, 70);")
        self.addstdnt = QtWidgets.QLabel(Dialog)
        self.addstdnt.setGeometry(QtCore.QRect(-140, 0, 831, 561))
        self.addstdnt.setStyleSheet("image: url(../MissingChild/images/bg5.png);")
        self.addstdnt.setText("")
        self.addstdnt.setObjectName("addstdnt")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 90, 201, 41))
        self.pushButton.setStyleSheet("font: 14pt \"Georgia\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.upload_photo)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 190, 201, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"Georgia\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.search_photo)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 290, 201, 41))
        self.pushButton_3.setStyleSheet("font: 14pt \"Georgia\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.messages)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AuthorityHome"))
        self.pushButton.setText(_translate("Dialog", "Upload Photo"))
        self.pushButton_2.setText(_translate("Dialog", "Search"))
        self.pushButton_3.setText(_translate("Dialog", "Message box"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
