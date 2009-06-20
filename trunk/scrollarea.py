#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robert Basic contactme@robertbasic.com"
__version__ = '0.0.1'

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ScrollArea(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.resize(300, 300)

        self.b = QPushButton('Add', self)
        self.connect(self.b, SIGNAL('clicked()'), self.add)

        self.w = QWidget(self)
        self.grid = QGridLayout(self.w)
        self.row = 0

        self.sa = QScrollArea(self)
        self.sa.setWidget(self.w)
        self.sa.setWidgetResizable(True)
        
        grid = QGridLayout(self)
        grid.addWidget(self.sa, 0, 0, 1, 1)
        grid.addWidget(self.b, 0, 1, 1, 1)


    def add(self):
        text = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        image = QImage('http://static.twitter.com/images/default_profile_normal.png')
        imageLabel = QLabel(self.w)
        #imageLabel.setText('http://static.twitter.com/images/default_profile_normal.png')
        imageLabel.setPixmap(QPixmap.fromImage(image))
        for t in text:
            label = QLabel(self.w)
            label.setText(t)

            line = QLabel(self.w)
            line.setFrameShape(QFrame.HLine)

            self.grid.addWidget(label, self.row, 0, 1, 1)
            self.grid.addWidget(imageLabel, self.row, 1, 1, 1)
            self.grid.addWidget(line, self.row+1, 0, 1, 2)

            self.row = self.row+2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    s = ScrollArea()
    s.show()
    sys.exit(app.exec_())
