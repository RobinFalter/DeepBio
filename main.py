import os
import openai
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

import speech_recognition as sr
import pyaudio
import pyttsx3

from view.main_ui import Ui_MainWindow
from model.utils.threads import SpeakTextWorker, Worker
from flask import Flask, redirect, render_template, request, url_for


class DeepBibUI(qtw.QMainWindow):
    def __init__(self):
        super(DeepBibUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.questions_answer_dict = {
            'Questions':["What is your name?",
             "Which is your gender?",
             "Do you have any nicknames?",
             "When and where were you born? Where did you live?",
             "When you were a child, what did you want to be when you grew up?",
             "What is your favourite hobby?",
             "What is your favourite travel destination? What did you like about that place?",
             "Are you married? If yes, what is your spouse's name?",
             "Do you have children? What are their names and ages?",
             "What kind of pets do you have, if any? What are their names?",
             "Are you a sports fan? If so, what is your favourite team?",
             "What causes are you passionate about?",
             "Did you attend college? If yes, what and when did you study?",
             "What drew you to your college or university major?",
             "Where did you work?",
             "Why do you like your job?",
             "How would you describe your career in three words?",
             "What professional accomplishment are you most proud of?",
             "What advice would you give to your younger self?",
             "What do you think is the key to professional success?",
             "What are the things you are very proud of?",
             "What was your greatest adventure?",
            ],
            'Answers': {}
        }
        for key, value in enumerate(self.questions_answer_dict['Questions']):
            self.questions_answer_dict['Answers'][key] = ''
        
        
        # self.questions_answered = {"Questions":[],"Answers":[]}
        
        self.question_index = 0
        self.threadpool = qtc.QThreadPool()
        self.threadpool.setMaxThreadCount(self.threadpool.maxThreadCount()-1)



        # Connect signals to actions
        self.ui.submitPushButton.clicked.connect(self.submit)
        self.ui.recordPushButton.clicked.connect(self.record)
        self.ui.createBibliographyButton.clicked.connect(self.create_biography)

        self.ui.SkipPushButton.clicked.connect(self.skip_question)
        self.ui.previousPushButton.clicked.connect(self.previous_question)
        self.ui.volumePushButton.clicked.connect(self.SpeakText)
        # self.create_speak_text_thread('Whats your name?')




    def submit(self):
        text = self.ui.responseTextEdit.toPlainText()
        # self.questions_answer_dict['Questions'].append(self.questions[self.question_index])
        self.questions_answer_dict['Answers'][self.question_index] = text
        # self.questions_answer_dict['Answers'].append(text)
        # self.questions_answer_dict['Answers'][] 
        print(self.questions_answer_dict)
        self.ui.responseTextEdit.setPlainText('')
        
        self.change_question()


    
    def record(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source,duration=2)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            self.ui.responseTextEdit.setPlainText(text)
            print(text)
        except Exception as e:
            print(e)

    def skip_question(self):
        self.question_index+=1
        self.ui.responseTextEdit.setPlainText('')
        self.questions_answer_dict['Answers'][self.question_index] = ''
        if self.question_index>=len(self.questions_answer_dict['Questions']):
            text = 'Well done you finished all the questions'
            self.ui.questionLabel.setText(text)
            return
        self.ui.questionLabel.setText(self.questions_answer_dict['Questions'][self.question_index])

    def previous_question(self):
        self.question_index-=1
        if self.question_index<0:
            self.question_index = 0

        # for index,item in enumerate(self.questions['Questions']):
        #     if item 

        # key = self.questions_answer_dict['Questions'] 
        
        self.ui.responseTextEdit.setPlainText(self.questions_answer_dict['Answers'][self.question_index])
        self.ui.questionLabel.setText(self.questions_answer_dict['Questions'][self.question_index])
    
    def change_question(self):
        self.question_index+=1
        if self.question_index>=len(self.questions_answer_dict['Questions']):
            self.ui.questionLabel.setText('Well done you finished all question')
            return
            
        self.ui.questionLabel.setText(self.questions_answer_dict['Questions'][self.question_index])

    def create_biography(self):
        response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=self.generate_prompt(),
                    temperature=0,
                    max_tokens = 300
                )
        trunc =  response['choices'][0]['text'].split('\n')[-1]
        self.ui.responseTextEdit.setPlainText(trunc)
        self.ui.questionLabel.setText('Your Biography')


    def generate_prompt(self):
        prompt = []

        for key, value in self.questions_answer_dict['Answers'].items():
            # if not(self.questions_answer_dict['Answers'][key]):
                prompt.append(self.questions_answer_dict['Questions'][key] + ' : ' + self.questions_answer_dict['Answers'][key] + ' ')
        prompt.append('Write a biography ' + str(self.questions_answer_dict['Answers'][0]))
        prompt = ''.join(prompt)
        print(prompt)
        return prompt

    # def create_speak_text_thread(self,text):
    #     create_speak_text_thread = Worker(self.SpeakText(text))
    #     self.threadpool.start(create_speak_text_thread)

    def SpeakText(self):
        print('started')
        text = self.questions_answer_dict['Questions'][self.question_index]
        # Initialize the engine
        engine = pyttsx3.init()
        #voices = engine.getProperty('voices')
        #engine.setProperty('voice', voices[0].id)
        engine.setProperty("rate", 100)
        engine.setProperty("Volume", 0.7)
        #time.sleep(3)
        engine.say(text)
        engine.runAndWait()

        
        # self.thread = qtc.QThread()
        # self.worker = SpeakTextWorker()
        # self.worker.moveToThread(self.thread)
        # self.thread.started.connect(lambda: self.worker.SpeakText(text))
        # self.thread.finished.connect(self.thread.quit)
        # self.thread.finished.connect(self.thread.deleteLater)
        # self.thread.finished.connect(self.worker.deleteLater)
        # self.thread.start()


if __name__ == '__main__':
    import sys
    openai.api_key = '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'
    app = qtw.QApplication(sys.argv)
    application = DeepBibUI()
    application.show()
    sys.exit(app.exec_())