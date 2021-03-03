import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from plyer import notification
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
 	notification.notify(
 	title = "WELCOME TO OMEGA",
 	message ="This a under devloping browser.\nWe hope you like it.\nThank you for donloading this browser.",
 	app_icon = "/home/aritra/Python Browser/omega.ico",
 	timeout= 12
 	)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        # navbar part 
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        home_btn = QAction('^^', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        forward_btn = QAction('>>', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())
    
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('OMEGA')
        self.setWindowIcon(QIcon('omega.png'))    

app = QApplication(sys.argv)
QApplication.setApplicationName('OMEGA')
window = MainWindow()
app.exec_()

