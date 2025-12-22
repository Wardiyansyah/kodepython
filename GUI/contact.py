from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
)
from EntryForm import *


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(450, 350)
        self.move(300, 300)
        self.setWindowTitle("Phonebook Manager")

        self.addButton = QPushButton("Tambah")
        self.editButton = QPushButton("Ubah")
        self.deleteButton = QPushButton("Hapus")
        self.clearButon = QPushButton("Kosongkan")
        self.exitButton = QPushButton("Keluar")

        hbox = QHBoxLayout()
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.editButton)
        hbox.addWidget(self.deleteButton)
        hbox.addWidget(self.clearButon)
        hbox.addWidget(self.exitButton)

        self.contactList = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.contactList)
        layout.addLayout(hbox)
        self.setLayout(layout)

        self.addButton.clicked.connect(self.addButtonClick)
        self.editButton.clicked.connect(self.editButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.clearButon.clicked.connect(self.contactList.clear)
        self.exitButton.clicked.connect(self.close)

    def addButtonClick(self):
        self.EntryForm = EntryForm()

        if self.EntryForm.exec_() == QDialog.Accepted:
            self.contactList.addItem(
                self.EntryForm.nameLineEdit.text()
                + " - "
                + self.EntryForm.phoneLineEdit.text()
            )

    def editButtonClick(self):
        if self.contactList.currentRow() < 0:
            return
        self.entryForm = EntryForm()
        s = str(self.contactList.currentItem().text())
        idx = s.index("-")
        self.entryForm.nameLineEdit.setText(s[: (idx - 1)])
        self.entryForm.phoneLineEdit.setText(s[(idx + 2) :])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.contactList.currentItem().setText(
                self.entryForm.nameLineEdit.text()
                + " - "
                + self.entryForm.phoneLineEdit.text()
            )

    def deleteButtonClick(self):
        row = self.contactList.currentRow()
        if row >= 0:
            self.contactList.takeItem(row)


if __name__ == "__main__":
    a = QApplication([])

    form = MainForm()
    form.show()

    a.exec_()
