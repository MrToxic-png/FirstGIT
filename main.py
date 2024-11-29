import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QDialog


class Painter(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        rand1 = randint(0, 50)
        rand2 = randint(0, 50)
        rand3 = randint(0, 50)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(30, 30, 150 + rand1, 150 + rand1)
        qp.drawEllipse(400, 30, 150 + rand2, 150 + rand2)
        qp.drawEllipse(800, 30, 150 + rand3, 150 + rand3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painter()
    ex.show()
    sys.exit(app.exec())
