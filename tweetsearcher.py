#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robert Basic contactme@robertbasic.com"
__version__ = '0.0.1'

import sys
import urllib2

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from tweetsearcherGui import *


class newSearch(QMdiSubWindow):
    
    searchTerm = "TweetSearcher"

    def __init__(self, parent):
        QMdiSubWindow.__init__(self)
        self.parent = parent
        self.parent.mdiArea.addSubWindow(self)
        self.gui = newSearchGui(self)


class tweetsearcher(QMainWindow):

    url = 'http://search.twitter.com/search.json?q='

    def __init__(self):
        QMainWindow.__init__(self)

        self.gui = tweetsearcherGui(self)

    def newSearchAction(self):
        newsearch = newSearch(self)
        newsearch.show()

    def settingsAction(self):
        pass

    def messageChanged(self):
        self.gui.statusMessage.setText('testing')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tsApp = tweetsearcher()
    tsApp.show()
    sys.exit(app.exec_())
