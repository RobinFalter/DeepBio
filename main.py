import os
import openai
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

import speech_recognition as sr
import pyttsx3

from model.utils.questionary import  QuestionaryBio, QuestionaryFam, QuestionaryMed, QuestionaryPro
from view.main_ui import Ui_MainWindow
from view.new_main_window_ui import Ui_NewMain


class NewMainWindow(qtw.QMainWindow):
    def __init__(self,key):
        super(NewMainWindow,self).__init__()
        self.ui = Ui_NewMain()
        self.ui.setupUi(self)
        self.key = key
        self.bio_window = QuestionaryBio(self.key)
        self.med_window = QuestionaryMed(self.key)
        self.pro_window = QuestionaryPro(self.key)
        self.fam_window = QuestionaryFam(self.key)


        self.ui.bioPushButton.clicked.connect(self.open_bio)
        self.ui.medPushButton.clicked.connect(self.open_med)
        self.ui.proPushButton.clicked.connect(self.open_prof)
        self.ui.famPushButton.clicked.connect(self.open_fam)


    def open_bio(self):
        self.bio_window.show()

    def open_med(self):
        self.med_window.show()

    def open_prof(self):
        self.pro_window.show()

    def open_fam(self):
        self.fam_window.show()


if __name__ == '__main__':
    import sys
    import json
    f = open('./config.json')
    key = json.load(f)
    openai.api_key = key['api-key']
    app = qtw.QApplication(sys.argv)
    application = NewMainWindow(key)
    application.showMaximized()
    sys.exit(app.exec_())