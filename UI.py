import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 497, 360)
        self.setWindowTitle('Yellow Circles')
        self.pushButton = QPushButton('Нажми на меня', self)
        self.pushButton.setGeometry(190, 250, 85, 23)