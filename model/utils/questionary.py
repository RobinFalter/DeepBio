import openai
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

import speech_recognition as sr
from fpdf import FPDF
import pyttsx3

from view.main_ui import Ui_MainWindow

class Questionary(qtw.QMainWindow):
    '''
    Questionary class defines functions attributes and functions to handle the questions asking process.
    Args: key(str) --> valid key to GPT3 OpenAI model
    '''
    def __init__(self,key):
        super(Questionary,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(qtg.QIcon('./view/images/deep_bio.jpeg'))
        self.setWindowTitle('Deep Bio')
        self.key = key
        self.question_index = 0
        self.type = ''
        self.trunc = ""
        self.submit_shortcut = qtw.QShortcut(qtg.QKeySequence('Ctrl+Return'),self)

        # Connect signals to actions
        self.ui.submitPushButton.clicked.connect(self.submit)
        self.submit_shortcut.activated.connect(self.submit)
        self.ui.recordPushButton.clicked.connect(self.record)
        self.ui.createBibliographyButton.clicked.connect(self.create_biography)
        self.ui.SkipPushButton.clicked.connect(self.skip_question)
        self.ui.previousPushButton.clicked.connect(self.previous_question)
        self.ui.volumePushButton.clicked.connect(self.SpeakText)
        self.ui.savePushButton.clicked.connect(self.save)

    def submit(self):
        '''Functions adds answer to questions_answer_dict'''
        text = self.ui.responseTextEdit.toPlainText()
        self.questions_answer_dict['Answers'][self.question_index] = text
        self.ui.responseTextEdit.setPlainText('')
        self.change_question()
    
    def record(self):
        '''Speech to text conversion for audio input'''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            self.ui.responseTextEdit.setPlainText(text)
        except Exception as e:
            print(e)

    def skip_question(self):
        '''Handles action of skip button'''
        self.question_index+=1
        self.set_empty_string()
        if self.question_index>=len(self.questions_answer_dict['Questions']):
            text = 'Well done you finished all the questions'
            self.ui.questionLabel.setText(text)
            return
        self.set_question_lable()

    def previous_question(self):
        '''Navigat to the previous question'''
        self.question_index-=1
        if self.question_index<0:
            self.question_index = 0
        self.set_question_lable()
        self.set_answer_plain_text()
        self.ui.savePushButton.setEnabled(False)
    
    def change_question(self):
        self.question_index+=1
        if self.question_index>=len(self.questions_answer_dict['Questions']):
            self.ui.questionLabel.setText('Well done you finished all question')
            return
        if not(self.questions_answer_dict['Answers'][self.question_index]==''):
            self.set_answer_plain_text()
        self.set_question_lable()

    def set_answer_plain_text(self):
        self.ui.responseTextEdit.setPlainText(self.questions_answer_dict['Answers'][self.question_index])

    def set_question_lable(self):
        self.ui.questionLabel.setText(self.questions_answer_dict['Questions'][self.question_index])

    def set_empty_string(self):
        self.ui.responseTextEdit.setPlainText('')
        self.questions_answer_dict['Answers'][self.question_index] = ''

    def create_biography(self):
            prompt = self.generate_prompt()
            action = [f"Write a biography about {str(self.questions_answer_dict['Answers'][0])} :", f"Add what {str(self.questions_answer_dict['Answers'][0])}  is passionate about", f"Describe {str(self.questions_answer_dict['Answers'][0])} education", f"What does {str(self.questions_answer_dict['Answers'][0])}  like to eat and how does he dress?"]
            self.trunc = ""
            for i in action:
                prompt += i
                response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt= prompt,
                            temperature=0,
                            max_tokens = 80
                        )
                prompt += response['choices'][0]['text'].split('\n')[-1]
                self.trunc +=  response['choices'][0]['text'].split('\n')[-1]
            self.ui.responseTextEdit.setPlainText(self.trunc)
            self.ui.questionLabel.setText('Biography')

    def generate_prompt(self):
        prompt = []
        for key, value in self.questions_answer_dict['Answers'].items():
            if self.questions_answer_dict['Answers'][key]!='':
                prompt.append(self.questions_answer_dict['Questions'][key] + ':' + self.questions_answer_dict['Answers'][key] + ' ')
        prompt.append('Write a biography ' + str(self.questions_answer_dict['Answers'][0]))
        prompt = ''.join(prompt)
        self.ui.savePushButton.setEnabled(True)
        return prompt

    def SpeakText(self):
        text = self.questions_answer_dict['Questions'][self.question_index]
        # Initialize the engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty("rate", 100)
        engine.setProperty("Volume", 0.7)
        engine.say(text)
        engine.runAndWait()

    def save(self):  
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = f"{self.type}", 
            ln = 1, align = 'C')
        pdf.multi_cell(0,8,txt=self.trunc,align='J')
        try:
            pdf.output(f"./output/{self.type}.pdf")   
            self.ui.questionLabel.setText('Successfully saved')
        except:
            print('Error saving pdf file')

    def initialize_dict(self):
        for key, value in enumerate(self.questions_answer_dict['Questions']):
                    self.questions_answer_dict['Answers'][key] = ''


class QuestionaryBio(Questionary):
    '''Biography subclass --> defines the questions for the category biograpy'''
    def __init__(self,key):
        super(QuestionaryBio,self).__init__(key)
        self.type = 'Biography'
        self.questions_answer_dict = {
            'Questions':["What is your name?",
            "What is your gender?",
            "Do you have any nicknames?",
            "When and where were you born? Where did you live?",
            "Are you married? If yes, what is your spouse's name?",
            "Do you have children? What are their names and ages?",
            "How did you grow up? Is there a childhood memory that you cherish?",
            "What is your favourite hobby? What were your favorite hobbies?",
            "What is your favourite travel destination? What did you like about that place?",
            "What kind of pets do you have, if any? What are their names?",
            "Are you a sports fan? If so, what is your favourite team?",
            "What causes are you passionate about?",
            "Did you attend college? If yes, what and when did you study?"
            "What drew you to your college or university major?",
            "Where did you work?",
            "Why do you like your job?",
            "What religion if any do you belong to? Would you describe yourself as being religious?",
            "What do you like to eat? What don't you like to eat?",
            "How do you like to dress? Do you have favourite clothes?",
            "Do you like to be among other people or do you prefer being on your own?",
            "What are the things you are very proud of?",
            "What was your greatest adventure?",
            "Is there anything you would like to add?"
            ],
            'Answers': {}
        }
        self.initialize_dict()

    def create_biography(self):
            prompt = self.generate_prompt()
            action = [f"Write a biography about {str(self.questions_answer_dict['Answers'][0])} :"]
            self.trunc = ""
            for i in action:
                prompt += i
                response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt= prompt,
                            temperature=0,
                            max_tokens = 300
                        )
                self.ui.questionLabel.setText('Your key expired. Get a new one')
                prompt += response['choices'][0]['text'].split('\n')[-1]
                self.trunc +=  response['choices'][0]['text'].split('\n')[-1]
            self.ui.responseTextEdit.setPlainText(self.trunc)
            self.ui.questionLabel.setText(self.type)

class QuestionaryMed(Questionary):
    '''Medical history subclass --> defines the questions for the category medical history'''
    def __init__(self,key):
        super(QuestionaryMed,self).__init__(key)
        self.trunc = ""
        self.type = 'Medical history'
        self.questions_answer_dict = {
            'Questions':['What is your name?',
            "Have you ever been rushed to the hospital in an ambulance? If Yes, do you remember why?",
            "Have you ever been treated in an emergency room?",
            "Have you ever had an allergic reaction to food, drug, insect or substance?",
            "Do you carry any medication in case of an emergency?",
            "Do you wear any medical jewellery like a bracelet?",
            "Do you have children? What are their names and ages?",
            "Have you taken tetanus in the last year?",
            "Have you experienced a fracture or sprain? If yes, where and how severe?",
            "Are you suffering from any complications/diseases at the moment?",
            "What Prescription and Non-Prescription Medications Do You Take?",
            "Do you have eyesight or hearing-related issues?",
            "What physical activities do you prefer to avoid?",
            ],
            'Answers': {}
        }
        self.initialize_dict()

    def create_biography(self):
            prompt = self.generate_prompt()
            action = [f"Write a medical report about {str(self.questions_answer_dict['Answers'][0])}"]
            for i in action:
                prompt += i
                response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt= prompt,
                            temperature=0,
                            max_tokens = 80
                        )
                self.ui.questionLabel.setText('Your key expired. Get a new one')
                prompt += response['choices'][0]['text'].split('\n')[-1]
                self.trunc +=  response['choices'][0]['text'].split('\n')[-1]
            self.ui.responseTextEdit.setPlainText(self.trunc)
            self.ui.questionLabel.setText(self.type)

class QuestionaryPro(Questionary):
    '''Profession history subclass --> defines the questions for the category profession history'''
    def __init__(self,key):
        self.trunc = ""
        self.type = 'Profession'
        super(QuestionaryPro,self).__init__(key)
        self.questions_answer_dict = {
            'Questions':["What is your name?",
            "What do you remember about the place you grew up?",
            "What was your first job?",
            "What was your favourite movie when you were younger?",
            "Which invention from your life are you most amazed by?",
            "What are the most important lessons you’ve learned in your life?",
            "Who has influenced you the most?",
            "If you could go back to any age, what would it be?",
            "If you’d like to go to the past and change something, what would that be?",
            "Which skills do you consider yourself an expert in?",
            "Would you be interested in sharing your knowledge with young people? Maybe they can learn from it.",
            ],
            'Answers': {}
        }
        self.initialize_dict()

    def create_biography(self):
            prompt = self.generate_prompt()
            action = [f"Write a report from the above information"]
            for i in action:
                prompt += i
                response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt= prompt,
                            temperature=0,
                            max_tokens = 80
                        )
                self.ui.questionLabel.setText('Your key expired. Get a new one')
                prompt += response['choices'][0]['text'].split('\n')[-1]
                self.trunc +=  response['choices'][0]['text'].split('\n')[-1]
            self.ui.responseTextEdit.setPlainText(self.trunc)
            self.ui.questionLabel.setText(self.type)

class QuestionaryFam(Questionary):
    '''Family history subclass --> defines the questions for the category family history'''
    def __init__(self,key):
        self.trunc = ""
        self.type = 'Family memories'
        super(QuestionaryFam,self).__init__(key)
        self.questions_answer_dict = {
            'Questions':["What is your name?",
            "Do you know the history of your family name, crest, or origin? If yes, would you like to share something?",
            "What do you remember about your parents and grandparents?",
            "What were your children like growing up? Do they have any funny or embarrassing stories about Mom or Dad?",
            "What did you and your siblings do for fun?",
            "How did you meet your spouse? Was it love at first sight or an uphill battle?",
            "What are your best memories with your parents?",
            "What are your best memories with your spouse?",
            "Did you have any family pets growing up?",
            "Did you remember any place that you visited and you liked a lot?",
            "If yes, how has that place changed from then?",
            "What would you like to advise your coming generations?Are you a sports fan? If so, what is your favourite team?",
            "How would you like to be remembered?",
            ],
            'Answers': {}
        }
        self.initialize_dict()

    def create_biography(self):
        '''Functions send request to GPT3-API and handles response'''
        prompt = self.generate_prompt()
        action = [f"Write a report from the above information"]
        for i in action:
            prompt += i
            response = openai.Completion.create(
                        engine="text-davinci-002",
                        prompt= prompt,
                        temperature=0,
                        max_tokens = 80
                    )
            prompt += response['choices'][0]['text'].split('\n')[-1]
            self.trunc +=  response['choices'][0]['text'].split('\n')[-1]
            self.ui.responseTextEdit.setPlainText(self.trunc)
            self.ui.questionLabel.setText(self.type)