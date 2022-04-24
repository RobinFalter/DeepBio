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
        self.setWindowIcon(qtg.QIcon('./view/images/deep_bio.jpeg'))
        self.setWindowTitle('Deep Bio')
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
        self.check_key()
        self.bio_window.show()

    def open_med(self):
        self.check_key()
        self.med_window.show()

    def open_prof(self):
        self.check_key()
        self.pro_window.show()

    def open_fam(self):
        self.check_key()
        self.fam_window.show()

    def check_key(self):
        try:
            response = openai.Completion.create(
                        engine="text-davinci-002",
                        prompt= 'Write test',
                        temperature=0,
                        max_tokens = 1
                    )
        except:
            msg = qtw.QMessageBox()
            msg.setIcon(qtw.QMessageBox.Information)
            msg.setText("Your GPT3 key expired")
            msg.setInformativeText("Get a new API key from the website")
            msg.setWindowTitle("Key expired error")
            msg.setStandardButtons(qtw.QMessageBox.Ok)
            retval = msg.exec_()
            quit()

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