__author__="Robert Basic contactme@robertbasic.com"

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class tweetsearcherGui():

    def __init__(self, parent=None):
        self.parent = parent
        parent.setObjectName("tweetsearcher")
        parent.resize(1000, 600)
        parent.setWindowTitle("tweetsearcher")
        parent.setWindowIcon(QIcon("icons/tweetsearcher.png"))

        parent.mdiArea = QMdiArea()
        parent.setCentralWidget(parent.mdiArea)

        parent.statusBar().showMessage("Welcome...")

        self.setupMenus()

    def setupMenus(self):

        self.setupFileMenu()

        ''' Create the MENUBAR '''
        menubar = self.parent.menuBar()
        
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(self.newSearch)
        fileMenu.addAction(self.settings)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exit)

    def setupFileMenu(self):
        ''' Actions for the FILE menu '''
        self.newSearch = QAction(QIcon("icons/new.png"), \
                                "&New search", \
                                self.parent)
        self.newSearch.setShortcut("Ctrl+N")
        self.parent.connect(self.newSearch, \
                            SIGNAL("triggered()"), \
                            self.parent.newSearchAction)
        self.settings = QAction(QIcon("icons/settings.png"), \
                                "Se&ttings", \
                                self.parent)
        self.settings.setShortcut("Ctrl+T")
        self.settings.setStatusTip("Change the settings of the application")
        self.parent.connect(self.settings, \
                            SIGNAL("triggered()"), \
                            self.parent.settingsAction)

        self.exit = QAction(QIcon("icons/exit.png"), \
                            "E&xit", \
                            self.parent)
        self.exit.setShortcut("Ctrl+Q")
        self.exit.setStatusTip("Exit the application")
        self.parent.connect(self.exit, \
                            SIGNAL("triggered()"), \
                            SLOT("close()"))

class newSearchGui():

    def __init__(self, parent):
        self.parent = parent
        self.parent.setAttribute(Qt.WA_DeleteOnClose)
        self.parent.resize(200, 200)
        self.parent.setWindowTitle("A new search for: " + parent.searchTerm)

        self.searchTermLineEdit = QLineEdit(self.parent)
