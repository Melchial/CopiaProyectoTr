# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/andre/Desktop/QTdesigner/SettingsGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 271)
        Form.setMinimumSize(QtCore.QSize(500, 271))
        Form.setMaximumSize(QtCore.QSize(500, 271))
        Form.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.translatePath = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.translatePath.setFont(font)
        self.translatePath.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.translatePath.setObjectName("translatePath")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.translatePath)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cropPath = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.cropPath.setFont(font)
        self.cropPath.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.cropPath.setObjectName("cropPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cropPath)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.deeplKey = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.deeplKey.setFont(font)
        self.deeplKey.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.deeplKey.setObjectName("deeplKey")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.deeplKey)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.consumerKey = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.consumerKey.setFont(font)
        self.consumerKey.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.consumerKey.setObjectName("consumerKey")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.consumerKey)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.consumerSecret = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.consumerSecret.setFont(font)
        self.consumerSecret.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.consumerSecret.setObjectName("consumerSecret")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.consumerSecret)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.accessToken = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.accessToken.setFont(font)
        self.accessToken.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.accessToken.setObjectName("accessToken")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.accessToken)
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.accessTokenSecret = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.accessTokenSecret.setFont(font)
        self.accessTokenSecret.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.accessTokenSecret.setObjectName("accessTokenSecret")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.accessTokenSecret)
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.bearerToken = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.bearerToken.setFont(font)
        self.bearerToken.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.bearerToken.setObjectName("bearerToken")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.bearerToken)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.saveSet = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveSet.sizePolicy().hasHeightForWidth())
        self.saveSet.setSizePolicy(sizePolicy)
        self.saveSet.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.saveSet.setFont(font)
        self.saveSet.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"border-radius: 10px;\n"
"width:60px;\n"
"height:30px;")
        self.saveSet.setObjectName("saveSet")
        self.verticalLayout_2.addWidget(self.saveSet, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_10.setText(_translate("Form", "Folder Paths"))
        self.label.setText(_translate("Form", "Translated Folder:"))
        self.label_2.setText(_translate("Form", "CropText Folder:"))
        self.label_3.setText(_translate("Form", "Download Path:"))
        self.label_4.setText(_translate("Form", "Twitter"))
        self.label_5.setText(_translate("Form", "Consumer key:"))
        self.label_6.setText(_translate("Form", "Consumer secret:"))
        self.label_7.setText(_translate("Form", "Access token:"))
        self.label_9.setText(_translate("Form", "Access token secret:"))
        self.label_8.setText(_translate("Form", "Bearer token:"))
        self.saveSet.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())