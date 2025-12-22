import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = QWidget()
    form.resize(300, 150)
    # form.move(300, 300)
    form.setWindowTitle("GUI Minimal")

    label = QLabel('<font color="blue" size="18">Hello World!</font>')
    # label.move(55, 40)
    label.setParent(form)

    form.show()

    app.exec_()
