import sys
from random import randint

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QDialog
from UI import Ui_Dialog


class Painter(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(30, 30, 150 + rand1, 150 + rand1)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(400, 30, 150 + rand2, 150 + rand2)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(800, 30, 150 + rand3, 150 + rand3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painter()
    ex.show()
    sys.exit(app.exec())
