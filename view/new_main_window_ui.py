# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewMain(object):
    def setupUi(self, NewMain):
        NewMain.setObjectName("NewMain")
        NewMain.resize(1980, 1080)
        NewMain.setStyleSheet("QWidget #centralwidget {\n"
"    background-color: #0F2333;\n"
"}\n"
"\n"
"QLabel#titleLabel {\n"
"    color: #FCFCFC;\n"
"}\n"
"\n"
"QPushButton#volumePushButton {\n"
"    background-color: #E50058;\n"
"    color: #FCFCFC;\n"
"    border-radius: 10px;\n"
"    min-width: 50px;\n"
"    min-height: 25px;\n"
"    font: 15px;\n"
"}\n"
"\n"
"QPushButton#volumePushButton:hover {\n"
"    background-color: #FF740F;\n"
"}\n"
"\n"
"QPushButton#volumePushButton:pressed {\n"
"    background-color:#FFBE36;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #E50058;\n"
"    color: #FCFCFC;\n"
"    border-radius: 20px;\n"
"    min-width: 100px;\n"
"    min-height: 50px;\n"
"    font: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FF740F;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:#FFBE36;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(NewMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_3.addItem(spacerItem)
        self.logoLabel = QtWidgets.QLabel(self.widget)
        self.logoLabel.setStyleSheet("image: url(:/newPrefix/images/deep_bio.jpeg);")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.verticalLayout_3.addWidget(self.logoLabel)
        self.titleLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_3.addWidget(self.titleLabel)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bioPushButton = QtWidgets.QPushButton(self.widget_3)
        self.bioPushButton.setObjectName("bioPushButton")
        self.verticalLayout_2.addWidget(self.bioPushButton)
        self.medPushButton = QtWidgets.QPushButton(self.widget_3)
        self.medPushButton.setObjectName("medPushButton")
        self.verticalLayout_2.addWidget(self.medPushButton)
        self.proPushButton = QtWidgets.QPushButton(self.widget_3)
        self.proPushButton.setObjectName("proPushButton")
        self.verticalLayout_2.addWidget(self.proPushButton)
        self.famPushButton = QtWidgets.QPushButton(self.widget_3)
        self.famPushButton.setObjectName("famPushButton")
        self.verticalLayout_2.addWidget(self.famPushButton)
        self.horizontalLayout_2.addWidget(self.widget_3)
        spacerItem2 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_2)
        NewMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewMain)
        QtCore.QMetaObject.connectSlotsByName(NewMain)

    def retranslateUi(self, NewMain):
        _translate = QtCore.QCoreApplication.translate
        NewMain.setWindowTitle(_translate("NewMain", "MainWindow"))
        self.titleLabel.setText(_translate("NewMain", "DeepBio"))
        self.bioPushButton.setText(_translate("NewMain", "Biography"))
        self.medPushButton.setText(_translate("NewMain", "Medical History"))
        self.proPushButton.setText(_translate("NewMain", "Professional And Life Knowledge"))
        self.famPushButton.setText(_translate("NewMain", "Family Memories"))
import title_img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewMain = QtWidgets.QMainWindow()
    ui = Ui_NewMain()
    ui.setupUi(NewMain)
    NewMain.show()
    sys.exit(app.exec_())
