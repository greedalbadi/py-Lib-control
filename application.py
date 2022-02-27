

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
import sys
import setupsys
import systimatic
from ub import TW
import time
import threading


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(586, 711)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.setWindowIcon(QtGui.QIcon('inapp.ico'))
        Form.setStyleSheet("background: rgb(0, 0, 0);")
        self.browsebox = QtWidgets.QLineEdit(Form)
        self.browsebox.setGeometry(QtCore.QRect(30, 190, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.browsebox.setFont(font)
        self.browsebox.setStyleSheet("background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"border-radius: 5px;\n"
"font-family: Courier New;\n"
"font-size: 20px;")
        self.browsebox.setInputMask("")
        self.browsebox.setText("")
        self.browsebox.setObjectName("browsebox")
        self.browsebtn = QtWidgets.QPushButton(Form)
        self.browsebtn.setGeometry(QtCore.QRect(480, 190, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.browsebtn.setFont(font)
        self.browsebtn.setStyleSheet("QPushButton#browsebtn{\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"font-family: Courier New;\n"
"font-size: 20px;\n"
"border-radius:4px;\n"
"}\n"
"QPushButton#browsebtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#browsebtn{\n"
"background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"}")
        self.browsebtn.setObjectName("browsebtn")
        self.userbox = QtWidgets.QLineEdit(Form)
        self.userbox.setGeometry(QtCore.QRect(30, 61, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.userbox.setFont(font)
        self.userbox.setStyleSheet("background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"border-radius: 5px;\n"
"font-family: Courier New;\n"
"font-size: 20px;")
        self.userbox.setInputMask("")
        self.userbox.setMaxLength(32766)
        self.userbox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.userbox.setObjectName("userbox")
        self.passwordbox = QtWidgets.QLineEdit(Form)
        self.passwordbox.setGeometry(QtCore.QRect(30, 110, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.passwordbox.setFont(font)
        self.passwordbox.setStyleSheet("background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"border-radius: 5px;\n"
"font-family: Courier New;\n"
"font-size: 20px;")
        self.passwordbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordbox.setObjectName("passwordbox")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(20, 400, 551, 231))
        font = QtGui.QFont()
        font.setFamily("Diwani Simple Striped")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: #ffffff;")
        self.textBrowser.setObjectName("textBrowser")
        self.versionbox = QtWidgets.QLineEdit(Form)
        self.versionbox.setGeometry(QtCore.QRect(60, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.versionbox.setFont(font)
        self.versionbox.setStyleSheet("background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"border-radius: 5px;\n"
"font-family: Courier New;\n"
"font-size: 20px;")
        self.versionbox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.versionbox.setObjectName("versionbox")
        self.builbox = QtWidgets.QLineEdit(Form)
        self.builbox.setGeometry(QtCore.QRect(240, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.builbox.setFont(font)
        self.builbox.setStyleSheet("background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"border-radius: 5px;\n"
"font-family: Courier New;\n"
"font-size: 20px;")
        self.builbox.setText("")
        self.builbox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.builbox.setObjectName("builbox")
        self.buildbtn = QtWidgets.QPushButton(Form)
        self.buildbtn.setGeometry(QtCore.QRect(30, 350, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.buildbtn.setFont(font)
        self.buildbtn.setStyleSheet("QPushButton#buildbtn{\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"font-family: Courier New;\n"
"font-size: 20px;\n"
"border-radius:6px;\n"
"}\n"
"QPushButton#buildbtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#buildbtn{\n"
"background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"}")
        self.buildbtn.setObjectName("buildbtn")
        self.uploadbtn = QtWidgets.QPushButton(Form)
        self.uploadbtn.setGeometry(QtCore.QRect(300, 350, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.uploadbtn.setFont(font)
        self.uploadbtn.setStyleSheet("QPushButton#uploadbtn{\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"font-family: Courier New;\n"
"font-size: 20px;\n"
"border-radius:6px;\n"
"}\n"
"QPushButton#uploadbtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#uploadbtn{\n"
"background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"}")
        self.uploadbtn.setObjectName("uploadbtn")
        self.builbox_2 = QtWidgets.QLineEdit(Form)
        self.builbox_2.setGeometry(QtCore.QRect(60, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.builbox_2.setFont(font)
        self.builbox_2.setStyleSheet("background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"border-radius: 5px;\n"
"font-family: Courier New;\n"
"font-size: 20px;")
        self.builbox_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.builbox_2.setObjectName("builbox_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 240, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 16px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 290, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 16px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 16px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 36, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 16px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 16px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 17px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(240, 240, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 15px;")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pyversionbox = QtWidgets.QLineEdit(Form)
        self.pyversionbox.setGeometry(QtCore.QRect(240, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.pyversionbox.setFont(font)
        self.pyversionbox.setStyleSheet("background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"border-radius: 5px;\n"
"font-family: Courier New;\n"
"font-size: 20px;")
        self.pyversionbox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pyversionbox.setObjectName("pyversionbox")
        self.undertextbtn = QtWidgets.QPushButton(Form)
        self.undertextbtn.setGeometry(QtCore.QRect(60, 650, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.undertextbtn.setFont(font)
        self.undertextbtn.setStyleSheet("QPushButton#undertextbtn{\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"font-family: Courier New;\n"
"font-size: 20px;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton#undertextbtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(242, 255, 0, 0.74);\n"
"color:rgba(0, 0, 0, 1);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#undertextbtn{\n"
"background-color:rgba(44, 40, 129, 0.8);\n"
"border:1px solid rgba(0,0,0,0);\n"
"color:rgba(255,255,255,0.5);\n"
"}")
        self.undertextbtn.setObjectName("undertextbtn")
        self.signedbox = QtWidgets.QCheckBox(Form)
        self.signedbox.setEnabled(True)
        self.signedbox.setGeometry(QtCore.QRect(230, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.signedbox.setFont(font)
        self.signedbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signedbox.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 13px;")
        self.signedbox.setChecked(True)
        self.signedbox.setObjectName("signedbox")
        self.fillbox = QtWidgets.QCheckBox(Form)
        self.fillbox.setGeometry(QtCore.QRect(420, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.fillbox.setFont(font)
        self.fillbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fillbox.setStyleSheet("color:rgba(255,255,255,0.5);\n"
"font-family: Courier New;\n"
"font-size: 17px;\n"
"border-radius:8px;")
        self.fillbox.setChecked(True)
        self.fillbox.setObjectName("fillbox")
        self.versionupdate = QtWidgets.QCheckBox(Form)
        self.versionupdate.setGeometry(QtCore.QRect(420, 300, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionupdate.sizePolicy().hasHeightForWidth())
        self.versionupdate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(-1)
        self.versionupdate.setFont(font)
        self.versionupdate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.versionupdate.setStyleSheet("color:rgba(255,255,255,0.5);\n"
"font-family: Courier New;\n"
"font-size: 21px;\n"
"border-size: 0px;\n"
"")
        self.versionupdate.setChecked(True)
        self.versionupdate.setTristate(False)
        self.versionupdate.setObjectName("versionupdate")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.browsebtn.setText(_translate("Form", "Browse"))
        self.userbox.setText(_translate("Form", "username"))
        self.passwordbox.setText(_translate("Form", "password"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Diwani Simple Striped\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.versionbox.setText(_translate("Form", "0.0.0"))
        self.buildbtn.setText(_translate("Form", "Build"))
        self.uploadbtn.setText(_translate("Form", "Upload"))
        self.builbox_2.setText(_translate("Form", "dist/*"))
        self.label.setText(_translate("Form", "Version (NR)"))
        self.label_2.setText(_translate("Form", "build (NR)"))
        self.label_3.setText(_translate("Form", "dist (NR)"))
        self.label_4.setText(_translate("Form", "pypi username (R)"))
        self.label_5.setText(_translate("Form", "pypi password (R)"))
        self.label_6.setText(_translate("Form", "Folder path (R)"))
        self.label_7.setText(_translate("Form", "Python Version (NR)"))
        self.pyversionbox.setText(_translate("Form", "0.0"))
        self.undertextbtn.setText(_translate("Form", "Open folder"))
        self.signedbox.setText(_translate("Form", "Stay signed"))
        self.fillbox.setText(_translate("Form", "Auto fill"))
        self.versionupdate.setText(_translate("Form", "AVU"))

class fuck_this_dumb_bug:

        def __init__(self):
                self.tw = TW()

class Form(QtWidgets.QWidget, Ui_Form):
        def __init__(self, *args, **kwargs):
                QtWidgets.QWidget.__init__(self, *args, **kwargs)
                self.setupUi(self)
                self.signedbox.setChecked(False)
                self.buildbtn.clicked.connect(self.builed)
                self.activestate()
                self.setWindowTitle("Lib control")
                self.undertextbtn.clicked.connect(self.openfolder)
                self.pyversionbox.setEnabled(False)
                self.uploadbtn.clicked.connect(self.upload)
                self.builbox.setEnabled(False)
                self.browsebtn.clicked.connect(self.getfolder)
                self.pyversionbox.setText(systimatic.getpy())
                self.textBrowser.setStyleSheet("color: #ffffff;\n"
"font-family: Courier New;\n"
"font-size: 14px;")


        def openfolder(self):

                return systimatic.openfolder(self.browsebox.text())

        def upload(self):
                def fthread():
                        self.undertextbtn.setText("working..")
                        self.disableallbtns()
                        records, status = TW().upload(self.browsebox.text(), self.userbox.text(), self.passwordbox.text(), self.builbox_2.text())

                        self.recordsloop(records)
                        self.enableallbtns()
                        self.default_status()
                threading.Thread(target=fthread).start()
                self.enableallbtns()
        def getfolder(self):
                self.browsebox.setText(systimatic.getfolder())
                threading.Thread(target=self.versionloop, daemon=True).start()
                return

        def activestate(self):

                def fthread():
                        while True:
                                if self.signedbox.checkState() == 2:

                                        try:
                                                if self.userbox.text() != "username" and self.passwordbox.text() != "password":
                                                        systimatic.writelog(self.userbox.text(), self.passwordbox.text())
                                                else:
                                                        username, password = systimatic.getlogdata(
                                                                username=self.userbox.text(),
                                                                password=self.passwordbox.text())

                                                        self.userbox.setText(username)
                                                        self.passwordbox.setText(password)
                                        except:
                                                pass
                                time.sleep(1)
                threading.Thread(target=fthread, daemon=True).start()



        def builed(self):
                def fthread():
                        self.undertextbtn.setText("working..")
                        self.disableallbtns()
                        self.textBrowser.append("Running builed function.")
                        records, result = TW().builed(self.browsebox.text(),
                                                    )
                        self.recordsloop(records)
                        self.enableallbtns()
                        self.default_status()
                threading.Thread(target=fthread, daemon=True).start()

        def recordsloop(self, records):
                for rec in records:
                        try:
                                self.textBrowser.append(rec)
                        except:
                                pass



        def change_status(self, status):

                return self.undertextbtn.setText(status)

        def default_status(self, status='Open Folder'):

                return self.undertextbtn.setText(status)

        def disableallbtns(self):

                self.browsebtn.setEnabled(False)
                self.buildbtn.setEnabled(False)
                self.uploadbtn.setEnabled(False)
                self.undertextbtn.setEnabled(False)

        def versionloop(self):
                def loop(old_version):
                        while True:

                                current_version = self.versionbox.text()
                                if old_version != current_version.replace(" ", ""):
                                        self.textBrowser.append(f"updated version: {current_version}")
                                        setupsys.setversion(self.browsebox.text(), current_version)
                                        print("break")
                                        break
                                time.sleep(1)

                while True:
                        if self.fillbox.checkState() == 2:
                                old_version = setupsys.getversion(self.browsebox.text())
                                self.versionbox.setText(old_version)
                                self.textBrowser.append(f"current version: {old_version}")
                                loop(old_version)



        def enableallbtns(self):
                self.browsebtn.setEnabled(True)
                self.buildbtn.setEnabled(True)
                self.uploadbtn.setEnabled(True)
                self.undertextbtn.setEnabled(True)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
