import os
import openai
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

import speech_recognition as sr
import pyaudio

from view.main_ui import Ui_MainWindow
from flask import Flask, redirect, render_template, request, url_for


class DeepBibUI(qtw.QMainWindow):
    def __init__(self):
        super(DeepBibUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.answer_question_dict = {
            'Questions': ["What is your name?",
             "Do you have any nicknames?",
             "When and where were you born?",
             "When you were a child, what did you want to be when you grew up?",
             "Where have you lived?",
             "What is your favourite hobby?",
             "What is your favourite travel destination? What did you like about that place?",
             "Are you married? If yes, what is your spouse's name?",
             "Do you have children? What are their names and ages?",
             "What kind of pets do you have, if any? What are their names?",
             "Are you a sports fan? If so, what is your favourite team?",
             "What causes are you passionate about?",
            #  "What is your highest level of education?",
             "Did you attend college? If yes, what and when did you study?"
             "What drew you to your college or university major?",
             "Where did you work?",
             "What other jobs have you had in your career?",
             "Why do you like your job?",
             "How would you describe your career in three words?",
             "What professional accomplishment are you most proud of?",
             "What advice would you give to your younger self?",
             "What do you think is the key to professional success?",
             "What are the things you are very proud of?",
             "What was your greatest adventure?",
             "Anything you would like to add?"
            ],
            'Answers': []
        }
        self.question_index = 0


        # Connect signals to actions
        self.ui.submitPushButton.clicked.connect(self.submit)
        self.ui.recordPushButton.clicked.connect(self.record)
        self.ui.createBibliographyButton.clicked.connect(self.create_bibliography)



    def submit(self):
        text = self.ui.responseTextEdit.toPlainText()
        self.answer_question_dict['Answers'].append(text)
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


    def change_question(self):
        self.question_index+=1
        if self.question_index>=len(self.answer_question_dict['Questions']):
            self.ui.questionLabel.setText('Well done you finished all question')
            return
            
        self.ui.questionLabel.setText(self.answer_question_dict['Questions'][self.question_index])

    def create_bibliography(self):
        response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=self.generate_prompt(),
                    temperature=0.6,
                )
        trunc =  response['choices'][0]['text'].split('\n')[-1]
        self.ui.responseTextEdit.setPlainText(trunc)



    def generate_prompt(self):
        prompt = ['Write a biography \n']
        for question, answer in zip(self.answer_question_dict['Questions'],self.answer_question_dict['Answers']):
            prompt.append(question + ' : ' + answer + '\n ')
        ''.join(prompt)
        return prompt

        # return f"""Write a biography
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # {self.answer_question_dict['Questions'][0]}: {self.answer_question_dict['Answers'][0]}
        # Nickname: {self.answer_question_dict['Answers'][0]}
        # Year of birth: {self.answer_question_dict['Answers'][1]}
        # Dream Job: {self.answer_question_dict['Answers'][2]}
        # Resident Adress: {self.answer_question_dict['Answers'][3]}
        # Hobby: {self.answer_question_dict['Answers'][4]}
        # Favorite travel destination: {self.answer_question_dict['Answers'][5]}
        # Married: {self.answer_question_dict['Answers'][6]}
        # Children: {self.answer_question_dict['Answers'][7]}
        # Name of pets: {self.answer_question_dict['Answers'][8]}
        # Favorite sports club: {self.answer_question_dict['Answers'][9]}
        # Passion: {self.answer_question_dict['Answers'][10]}
        # Highest Level of education: {self.answer_question_dict['Answers'][11]}
        # College or University: {self.answer_question_dict['Answers'][12]}
        # College time: {self.answer_question_dict['Answers'][13]}
        # Study subject: {self.answer_question_dict['Answers'][14]}
        # Reason for subject: {self.answer_question_dict['Answers'][15]}
        # Workplaces: {self.answer_question_dict['Answers'][16]}
        # Other jobs in carreer: {self.answer_question_dict['Answers'][17]}
        # Most import accomplishment: {self.answer_question_dict['Answers'][18]}
        # Advices to younger self: {self.answer_question_dict['Answers'][19]}
        # Key to professional success: {self.answer_question_dict['Answers'][20]}
        # Proud of: {self.answer_question_dict['Answers'][21]}
        # Greatest adventure: {self.answer_question_dict['Answers'][22]}
        # """


if __name__ == '__main__':
    import sys
    openai.api_key = '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'
    app = qtw.QApplication(sys.argv)
    application = DeepBibUI()
    application.show()
    sys.exit(app.exec_())