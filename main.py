import sys
from random import randint

from PyQt6 import uic
from PyQt6.QtCore import QPointF, QRectF, Qt
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QMainWindow, QApplication


class OMG(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.flag = False
        self.pushButton.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        for _ in range(randint(1, 10)):
            R = randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(QPointF(randint(100, 800), randint(100, 800)), R, R)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OMG()
    ex.show()
    sys.exit(app.exec())