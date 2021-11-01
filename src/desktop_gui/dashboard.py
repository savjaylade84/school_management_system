import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic
from settings import get_ui_link

class runApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(get_ui_link('dashboard'),self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    _try = runApp()
    _try.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing windown..')