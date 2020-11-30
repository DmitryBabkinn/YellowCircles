import sys
import time
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.press = False
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.clickButton)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_circles(qp)
        # Завершаем рисование
        qp.end()

    def draw_circles(self, qp):
        if self.press:
            qp.setBrush(QColor(255, 255, 0))
            x, y, d = randint(0, 450), randint(0, 360), randint(0, 366)
            qp.drawEllipse(x, y, d, d)

    def clickButton(self):
        self.press = True
        self.repaint()
        self.press = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())