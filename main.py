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
        self.circles = []
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.clickButton)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        if self.press:
            for i in self.circles:
                qp.setBrush(QColor(i[3], i[4], i[5]))
                qp.drawEllipse(i[0], i[1], i[2], i[2])
            x, y, d = randint(0, 450), randint(0, 360), randint(0, 366)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            self.circles.append(tuple([x, y, d, r, g, b]))
            qp.setBrush(QColor(r, g, b))
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