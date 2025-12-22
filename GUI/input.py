from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QLabel,
)


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle("Demo QGridLayout with Input")

        self.label1 = QLabel("Nama")
        self.lineEdit1 = QLineEdit()

        self.label2 = QLabel("No Handphone")
        self.lineEdit2 = QLineEdit()

        self.label3 = QLabel("")

        self.button1 = QPushButton("OK")

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.label3, 2, 0, 1, 2)
        layout.addWidget(self.button1, 3, 0, 1, 2)

        self.setLayout(layout)

        self.button1.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label3.setText(
            f"Nama: {self.lineEdit1.text()}, No Handphone: {self.lineEdit2.text()}"
        )


if __name__ == "__main__":
    app = QApplication([])

    form = MainForm()
    form.show()

    app.exec_()
