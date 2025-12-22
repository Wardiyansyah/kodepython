import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QMessageBox,
)


class LEDControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kontrol LED Arduino")
        self.setGeometry(300, 300, 250, 150)

        self.led_on_btn = QPushButton("Nyalakan LED")
        self.led_off_btn = QPushButton("Matikan LED")
        self.status_label = QLabel("Status: Tidak Terhubung")
        self.status_led = QLabel("Status LED: Tidak Aktif")

        layout = QVBoxLayout()
        layout.addWidget(self.led_on_btn)
        layout.addWidget(self.led_off_btn)
        layout.addWidget(self.status_led)
        layout.addWidget(self.status_label)
        self.setLayout(layout)

        self.led_on_btn.clicked.connect(self.turn_on_led)
        self.led_off_btn.clicked.connect(self.turn_off_led)

        # Otomatis mencari port Arduino
        self.arduino = self.find_arduino()
        if self.arduino:
            self.status_label.setText(f"Status: Terhubung ke {self.arduino.port}")
        else:
            QMessageBox.critical(self, "Error", "Arduino tidak ditemukan!")

    def find_arduino(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if (
                "Arduino" in port.description
                or "CH340" in port.description
                or "ttyACM" in port.description
            ):
                try:
                    return serial.Serial(port.device, 9600, timeout=1)
                except:
                    pass
        return None

    def turn_on_led(self):
        if self.arduino:
            self.arduino.write(b"1")
            self.status_led.setText("Status LED: Aktif")

    def turn_off_led(self):
        if self.arduino:
            self.arduino.write(b"0")
            self.status_led.setText("Status LED: Tidak Aktif")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LEDControlApp()
    window.show()
    sys.exit(app.exec_())
