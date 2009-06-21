#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robert Basic contactme@robertbasic.com"
__version__ = '0.0.1'

import sys
import urllib2
import webbrowser
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ScrollArea(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.resize(300, 300)

        self.b = QPushButton('&Add', self)
        self.connect(self.b, SIGNAL('clicked()'), self.add)

        self.w = QWidget(self)
        self.grid = QBoxLayout(QBoxLayout.TopToBottom, self.w)
        self.row = 0

        self.sa = QScrollArea(self)
        self.sa.setWidget(self.w)
        self.sa.setWidgetResizable(True)
        
        grid = QGridLayout(self)
        grid.addWidget(self.sa, 0, 0, 1, 1)
        grid.addWidget(self.b, 0, 1, 1, 1)

    def add(self):
        text = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        
        for t in text:
            label = QLabel(self.w)
            label.setOpenExternalLinks(True)
            label.setText("<a href=\"http://twitter.com/robertbasic\">@robertbasic</a>: %s" % self.row)

            line = QLabel(self.w)
            line.setFrameShape(QFrame.HLine)

            #self.grid.addWidget(label, self.row, 0, 1, 1)
            #self.grid.addWidget(line, self.row+1, 0, 1, 1)
            self.grid.insertWidget(0, label)
            self.grid.insertWidget(1, line)

            self.row = self.row+1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    s = ScrollArea()
    s.show()
    sys.exit(app.exec_())
