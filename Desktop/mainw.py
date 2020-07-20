import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtGui import QIcon


class MainW(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        showlButton = QPushButton("Show order list")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addWidget(showlButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 220, 800, 600)
        self.setWindowTitle('Jewelry Manager')
        self.setWindowIcon(QIcon('icon.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainW()
    sys.exit(app.exec_())