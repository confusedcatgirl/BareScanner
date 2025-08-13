from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtWebEngineWidgets
from PyQt6.QtCore import QUrl
from pathlib import Path
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Feelings App Prototype")
        
        view = QtWebEngineWidgets.QWebEngineView()
        html = Path('html\\index.html').read_text(encoding="utf8")
        view.setHtml(html, QUrl.fromLocalFile(os.getcwd() + os.path.sep + "html" + os.path.sep))
        self.setCentralWidget(view)
        self.showFullScreen()

app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec()