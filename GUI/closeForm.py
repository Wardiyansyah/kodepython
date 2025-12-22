from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle("Demo Menutup Form")

        self.button = QPushButton("Tutup")
        self.button.move(50, 50)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        super().close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = MainForm()
    form.show()

    app.exec_()

