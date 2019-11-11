import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt
import serial
import time

ser = serial.Serial(
    port='ttyACM0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
time.sleep(3)
print("connected to: " + ser.portstr)

#this will store the line
bline = []

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        self.b1 = QPushButton('Clear')
        self.b2 = QPushButton('Print')

        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(179)
        self.s1.setValue(90)
        self.s1.setTickInterval(5)
        self.s1.setTickPosition(QSlider.TicksBelow)

        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(1)
        self.s2.setMaximum(179)
        self.s2.setValue(90)
        self.s2.setTickInterval(5)
        self.s2.setTickPosition(QSlider.TicksBelow)

        self.s3 = QSlider(Qt.Horizontal)
        self.s3.setMinimum(1)
        self.s3.setMaximum(179)
        self.s3.setValue(90)
        self.s3.setTickInterval(5)
        self.s3.setTickPosition(QSlider.TicksBelow)

        self.s4 = QSlider(Qt.Horizontal)
        self.s4.setMinimum(1)
        self.s4.setMaximum(179)
        self.s4.setValue(90)
        self.s4.setTickInterval(5)
        self.s4.setTickPosition(QSlider.TicksBelow)

        self.s5 = QSlider(Qt.Horizontal)
        self.s5.setMinimum(1)
        self.s5.setMaximum(179)
        self.s5.setValue(90)
        self.s5.setTickInterval(5)
        self.s5.setTickPosition(QSlider.TicksBelow)


        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)
        v_box.addWidget(self.s2)
        v_box.addWidget(self.s3)
        v_box.addWidget(self.s4)
        v_box.addWidget(self.s5)


        self.setLayout(v_box)
        self.setWindowTitle('PyQt5 Lesson 8')

        self.b1.clicked.connect(lambda: self.btn_clk(self.b1, 'Hello from Clear'))
        self.b2.clicked.connect(lambda: self.btn_clk(self.b2, 'Hello from Print'))
        self.s1.valueChanged.connect(self.v1change)
        self.s1.valueChanged.connect(self.v2change)
        self.s1.valueChanged.connect(self.v3change)
        self.s1.valueChanged.connect(self.v4change)
        self.s1.valueChanged.connect(self.v5change)

        self.show()

    def btn_clk(self, b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def v1change(self):
        value = str(self.s1.value())
        self.le.setText(value)
        ser.write(str(value).encode())
        ser.write('\n'.encode())
        print(value);

    def v2change(self):
        value = str(self.s1.value())
        self.le.setText(value)
        ser.write(str(value).encode())
        ser.write('\n'.encode())
        print(value);

    def v3change(self):
        value = str(self.s1.value())
        self.le.setText(value)
        ser.write(str(value).encode())
        ser.write('\n'.encode())
        print(value);

    def v4change(self):
        value = str(self.s1.value())
        self.le.setText(value)
        ser.write(str(value).encode())
        ser.write('\n'.encode())
        print(value);

    def v4change(self):
        value = str(self.s1.value())
        self.le.setText(value)
        ser.write(str(value).encode())
        ser.write('\n'.encode())
        print(value);


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())