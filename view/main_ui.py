# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.questionLabel = QtWidgets.QLabel(self.widget)
        self.questionLabel.setObjectName("questionLabel")
        self.horizontalLayout_3.addWidget(self.questionLabel)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.responseTextEdit = QtWidgets.QPlainTextEdit(self.widget_3)
        self.responseTextEdit.setObjectName("responseTextEdit")
        self.horizontalLayout_2.addWidget(self.responseTextEdit)
        self.horizontalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignBottom)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SkipPushButton = QtWidgets.QPushButton(self.widget_4)
        self.SkipPushButton.setObjectName("SkipPushButton")
        self.verticalLayout_2.addWidget(self.SkipPushButton)
        self.recordPushButton = QtWidgets.QPushButton(self.widget_4)
        self.recordPushButton.setObjectName("recordPushButton")
        self.verticalLayout_2.addWidget(self.recordPushButton)
        self.submitPushButton = QtWidgets.QPushButton(self.widget_4)
        self.submitPushButton.setObjectName("submitPushButton")
        self.verticalLayout_2.addWidget(self.submitPushButton)
        self.createBibliographyButton = QtWidgets.QPushButton(self.widget_4)
        self.createBibliographyButton.setObjectName("createBibliographyButton")
        self.verticalLayout_2.addWidget(self.createBibliographyButton)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.questionLabel.setText(_translate("MainWindow", "What is your name? "))
        self.SkipPushButton.setText(_translate("MainWindow", "Skip"))
        self.recordPushButton.setText(_translate("MainWindow", "Record"))
        self.submitPushButton.setText(_translate("MainWindow", "Submit"))
        self.createBibliographyButton.setText(_translate("MainWindow", "Create Bio"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
