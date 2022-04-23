import traceback, sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw


class Worker(qtw.QObject):
    finished = qtw.pyqtSignal()



