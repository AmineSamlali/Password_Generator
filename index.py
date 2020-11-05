import string
import icons_rc
import random
import datetime
from PyQt5.QtGui import *
import webbrowser
from PyQt5.QtWidgets import QApplication
import clipboard
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from design import  Ui_MainWindow
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QIcon

"""
Program programmer : "Amine Samlali" 
mail : samlaliamine2@gmail.com
number phone = '212 619135651'
Donation On PayPal : https://paypal.me/AmineSamlali
"""

class MainApp(QMainWindow , Ui_MainWindow):
    def __init__(self ):
        super(MainApp , self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Connetions()
        self.checkBoxA = QCheckBox("Select This.")


    def Generate_Password(self):
        try:
            # handling the generating of Password
            pack_1 = 'abcdefghijklmnopqrstuvwxyz'
            pack_2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            pack_3 = '0123456789'
            pack_4 = string.punctuation
            value = self.spinBox.value()
            chackbox_1 = self.checkBox.isChecked()
            chackbox_2 = self.checkBox_2.isChecked()
            chackbox_3 = self.checkBox_3.isChecked()
            chackbox_4 = self.checkBox_4.isChecked()
            finel_pwd = ''
            if value != 0:
                if chackbox_1 == True :
                    for i in range(value):
                        finel_pwd += random.choice(pack_1)
                if chackbox_2 == True:
                    for i in range(value):
                        finel_pwd += random.choice(pack_2)
                if chackbox_3 == True:
                    for i in range(value):
                        finel_pwd += random.choice(pack_3)
                if chackbox_4 == True:
                    for i in range(value):
                        finel_pwd += random.choice(pack_4)
                empty_final_x = ''
                for i in range(len(finel_pwd)):
                    empty_final_x += random.choice(finel_pwd)
                if chackbox_1:
                    self.lineEdit.setText(empty_final_x)
                if chackbox_2:
                    self.lineEdit.setText(empty_final_x)
                if chackbox_3:
                    self.lineEdit.setText(empty_final_x)
                if chackbox_4:
                    self.lineEdit.setText(empty_final_x)

                if chackbox_1 and chackbox_2 and chackbox_3 and chackbox_4:
                    lenn = len(empty_final_x)/4
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x)

                if chackbox_3 and chackbox_2 or chackbox_2 and chackbox_4:
                    lenn = len(empty_final_x) / 2
                    indeex = round(lenn)

                    self.lineEdit.setText(empty_final_x[0:indeex])

                if chackbox_1 and chackbox_4:
                    lenn = len(empty_final_x) / 2
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])
                if chackbox_1 and chackbox_3:
                    lenn = len(empty_final_x) / 2
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])

                if chackbox_1 and chackbox_2:
                    lenn = (len(empty_final_x) / 2)
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])

                if chackbox_3 and chackbox_4:
                    lenn = len(empty_final_x) / 2
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])

                if chackbox_1 and chackbox_2 and chackbox_3:
                    lenn = len(empty_final_x) / 3
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])

                if chackbox_1 and chackbox_2 and chackbox_4:
                    lenn = len(empty_final_x) / 3
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])

                if chackbox_4 and chackbox_3 and chackbox_2:
                    lenn = len(empty_final_x) / 3
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])

                if chackbox_3 and chackbox_1 and chackbox_4:
                    lenn = len(empty_final_x) / 3
                    indeex = round(lenn)
                    self.lineEdit.setText(empty_final_x[0:indeex])


            elif chackbox_1 == False and chackbox_2 == False and chackbox_3 == False and chackbox_4 == False :
                self.lineEdit.setText("Please Check The Password options")
            else:
                self.lineEdit.setText("Please Enter A number ")
        except Exception:
            QMessageBox.information(self, "DOWNLOAD FAILED !! ", "PLEASE ENTER A CORRECT URL  PLEASE TRY AGAIN ❌❌")


    def copy(self):
        text = self.lineEdit.text()
        textx = text.strip()
        if 'Please Enter A number' in text:
            pass
        elif 'Please Check The Password options' in text:

            pass
        else:
            clipboard.copy(f"{textx}")

    def Add_To_Favorite(self):
        text = self.lineEdit.text()
        if len(text) == 0:
            pass
        elif 'Please Enter A number' in text:
            pass
        elif 'Please Check The Password options' in text:

            pass
        else:
            file = open('Password_Log.txt', 'a')
            # Handling Add on txt File
            text = self.lineEdit.text()
            file.write(f"Date:'{datetime.datetime.now()}' - Your password : {text}\n")
            file.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Done")
            msg.setText("You Password Has Been Added Successfully")
            msg.exec_()
            self.lineEdit.setText('')
            self.spinBox.setValue(0)
    def Donation(self):

        webbrowser.open('https://paypal.me/AmineSamlali')  # Go to example.com

    def Connetions(self):
        self.pushButton.clicked.connect(self.Generate_Password)
        self.pushButton_3.clicked.connect(self.copy)
        self.pushButton_2.clicked.connect(self.Donation)
        self.pushButton_4.clicked.connect(self.Add_To_Favorite)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


