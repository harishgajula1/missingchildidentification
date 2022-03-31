from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import sys
class Ui_Results(object):

    def view(self,found):

        try:

            self.found = found

            database = DBConnection.getConnection()
            cursor = database.cursor()


            sql2 = "select *from uploadphotos where cid='" + self.found + "' "
            cursor.execute(sql2)
            res = cursor.fetchall()

            for row in res:
                name1 = row[0]
                city1 = row[1]
                landmarks = row[2]
                remarks = row[3]
                photo = row[4]
                unm=row[5]
                role = row[6]

                print(self.found)
                print(photo)

                if role == "Officer":
                    sql = "select mno from authority where uid='" + unm + "' "
                    print(sql)
                    cursor.execute(sql)
                    cno = cursor.fetchone()[0]
                else:
                    sql = "select mno from users where uid='" + unm + "' "
                    print(sql)
                    cursor.execute(sql)
                    cno = cursor.fetchone()[0]

                self.name.setText(name1)
                self.city.setText(city1)
                self.lmarks.setText(landmarks)
                self.rmarks.setText(remarks)
                self.user.setText(unm + "("+role+")")
                self.mno.setText(cno)
                self.camera.setStyleSheet("image: url(../MissingChild/testimg/testingimg.jpg);")
                self.camera_2.setStyleSheet("image: url(../MissingChild/photos/"+str(self.found)+"/"+str(photo)+");")


        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)







    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 584)
        Dialog.setStyleSheet("background-color: rgb(136, 45, 68);")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(70, 90, 161, 131))
        self.camera.setStyleSheet("image: url(:/image/MissingChild/user.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 40, 181, 41))
        self.label_5.setStyleSheet("font: 11pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.camera_2 = QtWidgets.QLabel(Dialog)
        self.camera_2.setGeometry(QtCore.QRect(370, 90, 171, 131))
        self.camera_2.setStyleSheet("image: url(:/image/MissingChild/question-mark-face.jpg);")
        self.camera_2.setText("")
        self.camera_2.setObjectName("camera_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(390, 40, 181, 41))
        self.label_6.setStyleSheet("color: rgb(85, 170, 0);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 250, 141, 41))
        self.label.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(310, 290, 141, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 340, 141, 41))
        self.label_3.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 390, 141, 41))
        self.label_4.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(480, 240, 141, 51))
        self.name.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.name.setText("")
        self.name.setObjectName("name")
        self.city = QtWidgets.QLabel(Dialog)
        self.city.setGeometry(QtCore.QRect(480, 290, 131, 41))
        self.city.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.city.setText("")
        self.city.setObjectName("city")
        self.lmarks = QtWidgets.QLabel(Dialog)
        self.lmarks.setGeometry(QtCore.QRect(480, 340, 251, 41))
        self.lmarks.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.lmarks.setText("")
        self.lmarks.setObjectName("lmarks")
        self.rmarks = QtWidgets.QLabel(Dialog)
        self.rmarks.setGeometry(QtCore.QRect(480, 390, 251, 41))
        self.rmarks.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.rmarks.setText("")
        self.rmarks.setObjectName("rmarks")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(310, 450, 141, 41))
        self.label_11.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.user = QtWidgets.QLabel(Dialog)
        self.user.setGeometry(QtCore.QRect(480, 450, 251, 41))
        self.user.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.user.setText("")
        self.user.setObjectName("user")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(310, 500, 141, 41))
        self.label_13.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.mno = QtWidgets.QLabel(Dialog)
        self.mno.setGeometry(QtCore.QRect(480, 500, 251, 41))
        self.mno.setStyleSheet("font: 75 12pt \"Vani\";\n"
"color: rgb(255, 255, 255);")
        self.mno.setText("")
        self.mno.setObjectName("mno")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Searching Photo"))
        self.label_6.setText(_translate("Dialog", "Matching Found"))
        self.label.setText(_translate("Dialog", "Name                :"))
        self.label_2.setText(_translate("Dialog", "City                    :"))
        self.label_3.setText(_translate("Dialog", "Landmarks       :"))
        self.label_4.setText(_translate("Dialog", "Remarks           :"))
        self.label_11.setText(_translate("Dialog", "Uploaded by     :"))
        self.label_13.setText(_translate("Dialog", "Contact Number   :"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
