from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 350)
        self.setWindowTitle("Grade Nilai")

        self.labelNama = QLabel("Nama")
        self.nama = QLineEdit()

        self.labelMatkul = QLabel("Mata Kuliah")
        self.matkul = QLineEdit()

        self.labelEtika = QLabel("Nilai Etika")
        self.etika = QLineEdit()

        self.labelKehadiran = QLabel("Jumlah Kehadiran")
        self.kehadiran = QLineEdit()

        self.labelTugas = QLabel("Nilai Tugas")
        self.tugas = QLineEdit()

        self.labelUTS = QLabel("Nilai UTS")
        self.uts = QLineEdit()

        self.labelUAS = QLabel("Nilai UAS")
        self.uas = QLineEdit()

        self.labelBobot = QLabel("<center><h1>Bobot Nilai</h1></center>")
        self.labelBobot.setStyleSheet("""
            color: blue;
            border: 2px solid black;
        """)

        self.labelBetika = QLabel("Bobot Etika")
        self.bEtika = QLineEdit()

        self.labelBkehadiran = QLabel("Bobot Kehadiran")
        self.bKehadiran = QLineEdit()

        self.labelBtugas = QLabel("Bobot Tugas")
        self.bTugas = QLineEdit()

        self.labelButs = QLabel("Bobot UTS")
        self.bUTS = QLineEdit()

        self.labelBuas = QLabel("Bobot UAS")
        self.bUAS = QLineEdit()

        # nilai_akhir = (
        # int(self.etika.text()) * (int(self.bEtika.text()) / float(100))
        # + ((int(self.kehadiran.text()) / 16) * 100)
        # * (int(self.bKehadiran.text()) / float(100))
        # + int(self.tugas.text()) * (int(self.bTugas.text()) / float(100))
        # + int(self.uts.text()) * (int(self.bUTS.text()) / float(100))
        # + int(self.uas.text()) * (int(self.bUAS.text()) / float(100))
        # )

        self.buttonHitung = QPushButton("Hitung Nilai")
        self.buttonHitung.setStyleSheet("""
        background-color: lightgreen;
        color: black;
        font-weight: bold;
        padding: 10px;
        font-size: 18px;
        """)

        grid = QGridLayout()
        grid.addWidget(self.labelNama, 0, 0)
        grid.addWidget(self.nama, 0, 1)
        grid.addWidget(self.labelMatkul, 1, 0)
        grid.addWidget(self.matkul, 1, 1)
        grid.addWidget(self.labelEtika, 2, 0)
        grid.addWidget(self.etika, 2, 1)
        grid.addWidget(self.labelKehadiran, 3, 0)
        grid.addWidget(self.kehadiran, 3, 1)
        grid.addWidget(self.labelTugas, 4, 0)
        grid.addWidget(self.tugas, 4, 1)
        grid.addWidget(self.labelUTS, 5, 0)
        grid.addWidget(self.uts, 5, 1)
        grid.addWidget(self.labelUAS, 6, 0)
        grid.addWidget(self.uas, 6, 1)
        grid.addWidget(self.buttonHitung, 7, 0, 1, 4)

        grid.addWidget(self.labelBobot, 0, 2, 2, 2)
        grid.addWidget(self.labelBetika, 2, 2)
        grid.addWidget(self.bEtika, 2, 3)
        grid.addWidget(self.labelBkehadiran, 3, 2)
        grid.addWidget(self.bKehadiran, 3, 3)
        grid.addWidget(self.labelBtugas, 4, 2)
        grid.addWidget(self.bTugas, 4, 3)
        grid.addWidget(self.labelButs, 5, 2)
        grid.addWidget(self.bUTS, 5, 3)
        grid.addWidget(self.labelBuas, 6, 2)
        grid.addWidget(self.bUAS, 6, 3)

        self.setLayout(grid)


if __name__ == "__main__":
    app = QApplication([])

    form = MainForm()
    form.show()

    app.exec_()
