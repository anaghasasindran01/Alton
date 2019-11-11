from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt
import serial
import time

ser1 = serial.Serial("/dev/ttyACM0",9600, writeTimeout = 0)

time.sleep(3)
print("connected to: " + ser1.portstr)

#this will store the line
bline = []

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.le = QLineEdit()
        #self.b1 = QPushButton('Clear')
        #self.b2 = QPushButton('Print')

        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(179)
        self.s1.setValue(1)
        self.s1.setTickInterval(5)
        self.s1.setTickPosition(QSlider.TicksBelow)

        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(1)
        self.s2.setMaximum(179)
        self.s2.setValue(1)
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

        '''self.s6 = QSlider(Qt.Horizontal)
        self.s6.setMinimum(0)
        self.s6.setMaximum(179)
        self.s6.setValue(179)
        self.s6.setTickInterval(5)
        self.s6.setTickPosition(QSlider.TicksBelow)'''

        self.s6 = QtWidgets.QPushButton(self)
        self.s6.setGeometry(QtCore.QRect(850, 930, 120, 80))
        self.s6.setText("GRIPPER ON")
        self.s6.setObjectName("on")

        self.s7 = QtWidgets.QPushButton(self)
        self.s7.setGeometry(QtCore.QRect(950, 930, 80, 80))
        self.s7.setText("GRIPPER OFF")
        self.s7.setObjectName("off")

        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        #v_box.addWidget(self.b1)
        #v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)
        v_box.addWidget(self.s2)
        v_box.addWidget(self.s3)
        v_box.addWidget(self.s4)
        v_box.addWidget(self.s5)
        #v_box.addWidget(self.s6)
        #v_box.addWidget(self.s7)

        self.setLayout(v_box)
        self.setWindowTitle('Arm motors')

        #self.b1.clicked.connect(lambda: self.btn_clk(self.b1, 'Hello from Clear'))
        #self.b2.clicked.connect(lambda: self.btn_clk(self.b2, 'Hello from Print'))
        self.s1.valueChanged.connect(self.v1change)
        self.s2.valueChanged.connect(self.v2change)
        self.s3.valueChanged.connect(self.v3change)
        self.s4.valueChanged.connect(self.v4change)
        self.s5.valueChanged.connect(self.v5change)
        self.s6.clicked.connect(self.v6change)
        self.s7.clicked.connect(self.v7change)

        self.show()

    def btn_clk(self, b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def v1change(self, value):
        print("shoulder x motor")

        value = str(self.s1.value())
        self.le.setText(value)
        print(value)

        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'R5\n'))
        ser1.write(bytes(b'R5\n'))

        data = "A{}\n".format(value)
        print("output = '" + data + "'")
        ser1.write(data.encode())


    def v2change(self, value):
        print("shoulder y motor")

        value = str(self.s2.value())
        self.le.setText(value)
        print(value)


        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'R6\n'))
        ser1.write(bytes(b'R6\n'))

        data = "B{}\n".format(value)
        print("output = '" + data + "'")
        ser1.write(data.encode())

    def v3change(self, value):
        print("knee x motor")

        value = str(self.s3.value())
        self.le.setText(value)
        #print(value)


        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'R7\n'))
        ser1.write(bytes(b'R7\n'))

        data = "C{}\n".format(value)
        print("output = '" + data + "'")
        ser1.write(data.encode())

    def v4change(self, value):
        print("knee Y motor")

        value = str(self.s4.value())
        self.le.setText(value)
        print(value)

        print(value)
        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'R8\n'))
        ser1.write(bytes(b'R8\n'))

        data = "D{}\n".format(value)
        print("output = '" + data + "'")
        ser1.write(data.encode())

    def v5change(self, value):
        print("wrist x motor")

        value = str(self.s5.value())
        self.le.setText(value)
        print(value)

        print(value)
        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'R9\n'))
        ser1.write(bytes(b'R9\n'))

        data = "E{}\n".format(value)
        print("output = '" + data + "'")
        ser1.write(data.encode())

    def v6change(self):
        print("grab on button clicked")
        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'R10\n'))
        ser1.write(bytes(b'R10\n'))


    def v7change(self):
        print("grab off button clicked")
        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'R11\n'))
        ser1.write(bytes(b'R11\n'))



app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
