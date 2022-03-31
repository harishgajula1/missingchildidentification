

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,sys,os
from ChildIdentification import predict,show_prediction_labels_on_image,train
from Result import Ui_Results
class Ui_Search(object):
    def __init__(self, Dialog, unm):
        self.dialog = Dialog
        self.unm = unm

    def browse_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Photo")
        print(fileName)
        self.lineEdit.setText(fileName)

    def search(self):
        try:

            namelist = []
            namelist.clear()
            photo=self.lineEdit.text()


            if photo == "" or photo == "null" :
                self.showMessageBox("Information", "Please select photo")

            else:
                imgdata = self.read_file(photo)
                self.write_file(imgdata)

                print("Training KNN classifier...")
                classifier = train("../MissingChild/photos", model_save_path="trained_knn_model.clf", n_neighbors=1)
                print("Training complete!")

                # STEP 2: Using the trained classifier, make predictions for unknown images
                for image_file in os.listdir("../MissingChild/testimg"):
                    full_file_path = os.path.join("../MissingChild/testimg", image_file)

                    print("Looking for faces in {}".format(image_file))

                    # Find all people in the image using a trained classifier model
                    # Note: You can pass in either a classifier file name or a classifier model instance
                    predictions = predict(full_file_path, model_path="trained_knn_model.clf")

                    # Print results on the console
                    for name, (top, right, bottom, left) in predictions:
                        namelist.append(name)
                        print("- Found {} at ({}, {})".format(name, left, top))

                    # Display results overlaid on an image
                    #show_prediction_labels_on_image(os.path.join("../MissingChild/testimg", image_file), predictions)

                print(namelist)
                # self.setNames(namelist)
                '''database = DBConnection.getConnection()
                cursor = database.cursor()
                for nm in namelist:
                    sql = "insert into temp values('" + str(nm) + "')"
                    cursor.execute(sql)
                    database.commit()'''


                if len(namelist)==0 or namelist[0]=="unknown":
                    self.showMessageBox("Information", "No Results Found")

                else:
                    try:
                        self.photo = QtWidgets.QDialog()
                        self.ui = Ui_Results()
                        self.ui.setupUi(self.photo)
                        self.ui.view(namelist[0])
                        self.photo.show()
                        self.dialog.hide()

                    except Exception as e:
                        print(e.args[0])
                        tb = sys.exc_info()[2]
                        print(tb.tb_lineno)




        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def read_file(self, filename):
        with open(filename, 'rb') as f:
            img = f.read()
        return img

    def write_file(self,data):
        with open("../MissingChild/testimg/testingimg.jpg", 'wb') as f:
            f.write(data)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 409)
        Dialog.setStyleSheet("background-color: rgb(113, 75, 56);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 60, 301, 71))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Georgia\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 101, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Georgia\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 291, 31))
        self.lineEdit.setStyleSheet("font: 75 10pt \"Verdana\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(420, 170, 91, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Georgia\";\n"
"background-color: rgb(57, 115, 172);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 230, 121, 31))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Georgia\";\n"
"background-color: rgb(47, 200, 60);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.search)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Search Missing Child"))
        self.label_2.setText(_translate("Dialog", "Select Photo"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton_3.setText(_translate("Dialog", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
