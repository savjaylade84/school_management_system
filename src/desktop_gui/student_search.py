import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic

class student_search(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Student_Search.ui',self)