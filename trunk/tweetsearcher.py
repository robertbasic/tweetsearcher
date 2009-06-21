#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robert Basic contactme@robertbasic.com"
__version__ = '0.0.1'

import sys
import urllib2

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from tweetsearcherGui import *


class searchWindow(QMdiSubWindow):
    
    searchTerm = ""
    row = 100
    labels = []

    def __init__(self, parent):
        QMdiSubWindow.__init__(self)
        self.parent = parent
        self.parent.mdiArea.addSubWindow(self)

        self.gui = searchWindowGui(self)

    def applySearchTerm(self):
        text = ['a', 'b', 'c']
        #text.reverse()

        for t in text:
            label = QLabel(self.gui.scrollAreaWidget)
            label.setMaximumHeight(100)
            label.resize(label.width(), 200)
            label.setText(t)
            line = QLabel(self.gui.scrollAreaWidget)
            line.setFrameShape(QFrame.HLine)

            self.gui.scrollAreaGrid.addWidget(label, self.row, 0, 1, 1, Qt.AlignTop)
            self.gui.scrollAreaGrid.addWidget(line, self.row-1, 0, 1, 1, Qt.AlignTop)
            self.row = self.row-2


class tweetsearcher(QMainWindow):

    url = 'http://search.twitter.com/search.json?q='

    def __init__(self):
        QMainWindow.__init__(self)

        self.gui = tweetsearcherGui(self)

    def newSearchAction(self):
        searchwindow = searchWindow(self)
        searchwindow.show()

    def settingsAction(self):
        pass

    def messageChanged(self):
        self.gui.statusMessage.setText('testing')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tsApp = tweetsearcher()
    tsApp.show()
    sys.exit(app.exec_())
