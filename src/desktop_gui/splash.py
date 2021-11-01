import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic

class splash(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/Splash.ui',self)