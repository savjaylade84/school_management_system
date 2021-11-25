from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from desktop_gui.settings import get_ui_link

class student_search(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(get_ui_link('student_search'),self)