from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        # self.move(300, 300)
        self.setWindowTitle("Demo QVGridLayout")

        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        self.button4 = QPushButton("Button 4")

        layout = QGridLayout()
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 0, 1)
        layout.addWidget(self.button3, 1, 0)
        layout.addWidget(self.button4, 1, 1)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])

    form = MainForm()
    form.show()

    app.exec_()
