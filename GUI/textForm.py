from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDesktopWidget


class TextForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.center()
        self.setWindowTitle("Demo Tag HTML")

        self.label1 = QLabel("<h1>Hello <font color='red'>World!</font></h1>")
        self.label1.move(10, 10)
        self.label1.setParent(self)

        self.label2 = QLabel("""
        Contoh teks <b>tebal</b>, <i>miring</i>, dan <u>garis bawah</u>.<br>
        <a href='www.google.com'>google.com</a> adalah contoh link.
        """)
        self.label2.setWordWrap(True)
        self.label2.move(10, 50)
        self.label2.setParent(self)

        self.button = QPushButton("Tutup")
        self.button.move(10, 150)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

        self.button.setStyleSheet(
            "background-color: yellow; color: black; font-weight: bold;"
        )
        self.setStyleSheet("background-color: aqua")

    def buttonClick(self):
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication([])

    form = TextForm()
    form.show()

    app.exec_()
