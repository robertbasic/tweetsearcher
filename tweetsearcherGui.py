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

        parent.statusBar().showMessage('Hello')

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

class searchWindowGui():

    def __init__(self, parent):
        self.parent = parent
        self.parent.setAttribute(Qt.WA_DeleteOnClose)

        self.parent.resize(300, 500)
        self.parent.setMinimumWidth(300)
        self.parent.setMaximumWidth(500)
        self.parent.setMinimumHeight(300)

        self.parent.setWindowTitle("Search for: " + parent.searchTerm)

        self.centralWidget = QWidget(self.parent)
        self.parent.setWidget(self.centralWidget)

        self.scrollAreaWidget = QWidget(self.parent)

        self.scrollArea = QScrollArea(self.centralWidget)
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaGrid = QGridLayout(self.scrollAreaWidget)

        self.searchTermLine = QLineEdit(self.centralWidget)

        self.applySearchTermButton = QPushButton(QIcon(), \
                                                QString('&Apply'), \
                                                self.centralWidget)
        self.parent.connect(self.applySearchTermButton, \
                            SIGNAL("clicked()"), \
                            self.parent.applySearchTerm)

        self.closeButton = QPushButton(QIcon(), \
                                        QString('Close'), \
                                        self.centralWidget)
        self.parent.connect(self.closeButton, \
                            SIGNAL("clicked()"), \
                            SLOT("close()"))

        grid = QGridLayout(self.centralWidget)
        grid.addWidget(self.searchTermLine, 0, 0, 1, 1)
        grid.addWidget(self.applySearchTermButton, 0, 1, 1, 1)
        grid.addWidget(self.scrollArea, 1, 0, 1, 2)
        grid.addWidget(self.closeButton, 2, 0, 1, 2, Qt.AlignBottom)
