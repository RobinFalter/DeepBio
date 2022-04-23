import traceback, sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
import pyttsx3


class Worker(qtc.QRunnable):
    def __init__(self,fn,*args,**kwargs):
        super(Worker,self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @qtc.pyqtSlot()
    def run(self):
        self.fn(*self.args,**self.kwargs)

class SpeakTextWorker(qtc.QObject):
    finished = qtc.pyqtSignal()

    def SpeakText(self,text):

        print('started')
        # Initialize the engine
        engine = pyttsx3.init()
        #voices = engine.getProperty('voices')
        #engine.setProperty('voice', voices[0].id)
        engine.setProperty("rate", 100)
        engine.setProperty("Volume", 0.7)
        #time.sleep(3)
        engine.say(text)
        engine.runAndWait()
        self.finished.emit()



