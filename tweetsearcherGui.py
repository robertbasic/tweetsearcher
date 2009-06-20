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

        self.statusMessage = QLabel()
        #self.statusMessage.setFrameStyle(QFrame.Sunken)
        self.statusMessage.setText('Ready...')
        self.status = QLabel()
        self.status.setToolTip('Connection')
        #self.status.setFrameStyle(QFrame.Sunken)
        #self.status.setText('Ready...')
        icon = QPixmap()
        icon.load('bell.png')
        self.status.setPixmap(icon)
        parent.statusBar().insertPermanentWidget(0, self.statusMessage, 0)
        parent.statusBar().addPermanentWidget(self.status, 0)
        parent.statusBar().showMessage('Hello')
        parent.statusBar().setSizeGripEnabled(False)

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
        self.parent.resize(200, 550)
        self.parent.setMinimumWidth(200)
        self.parent.setMinimumWidth(300)
        #self.parent.setWindowFlags(Qt.WindowShadeButtonHint)
        self.parent.setWindowTitle("A new search for: " + parent.searchTerm)

        self.widget = QWidget(self.parent)
        self.widget.setAttribute(Qt.WA_DeleteOnClose)
        self.parent.setWidget(self.widget)

        self.searchTermLineEdit = QLineEdit(self.parent)
        self.labelOne = QTextBrowser(self.parent)
        self.labelOne.setText(QString('First label label laeasdkj lasowd as owedoi oi oiusodiuowieur od foiuoiuwq eoiu oiuoifudsoifu woieuoiu <a href="http://google.com">dpafosiduf</a> oi wueoifu opi dhoiufoiwue ofi'))
        self.labelOne.setReadOnly(True)
        self.labelTwo = QLabel(QString('Second label'), self.parent)

        self.button = QPushButton(QString('Close'), self.parent)
        self.parent.connect(self.button, SIGNAL("clicked()"), SLOT("close()"))

        grid = QGridLayout(self.widget)
        grid.addWidget(self.searchTermLineEdit, 0, 0, 1, 2)
        grid.addWidget(self.labelOne, 1, 0, 1, 1, Qt.AlignTop)
        grid.addWidget(self.labelTwo, 1, 1, 1, 1, Qt.AlignTop)
        grid.addWidget(self.button, 2, 0, 1, 2, Qt.AlignBottom)
