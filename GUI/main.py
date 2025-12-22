import sys
from PyQt5.QtWidgets import QApplication

from MainForm import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = MainForm()
    form.show()

    app.exec_()
