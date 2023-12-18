# GUI Demo using PyQt

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First PyQtGUI App")
        self.button = QPushButton("Press Me")

        self.setCentralWidget(self.button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
		
