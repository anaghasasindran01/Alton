import serial
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import signal
import threading
from time import sleep
from threading import Timer

#ser1 = serial.Serial("/dev/ttyUSB0",9600, writeTimeout = 0) # base arduino
#ser2 = serial.Serial("/dev/ttyACM0",9600, writeTimeout = 0) # head ardino and led
#ser3 = serial.Serial("/dev/ttyACM1",9600, writeTimeout = 0) # right hand arduino
#ser4 = serial.Serial("/dev/ttyACM2",9600, writeTimeout = 0) # left hand arduino

class startWindow(QtWidgets.QWidget):

    start_sig = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Start Window')
        self.setFixedSize(640, 480)
        self.p = 0
        self.t = 0

        self.start = QtWidgets.QPushButton(self)
        self.start.setGeometry(QtCore.QRect(350, 140, 140, 140))
        self.start.setText("TOUCH ME")
        self.start.setObjectName("start")

        self.start.clicked.connect(self.switch1)
        self.serial_read_thread1 = threading.Thread(target=self.read_from_port, args=(ser2,))
        self.serial_read_thread1.start()
        self.serial_read_thread2 = threading.Thread(target=self.read_from_port, args=(ser1,))
        self.serial_read_thread2.start()
        self.serial_read_thread3 = threading.Thread(target=self.read_from_port, args=(ser3,))
        self.serial_read_thread3.start()

    def switch1(self):
        #led arduino(head)
        print("Alton is powered on")
        print("Chest and head Lights on")
        ser2.flushInput()
        ser2.flushOutput()
        ser2.write(bytes(b'C1\n'))
        ser2.write(bytes(b'C1\n'))
        self.start.setEnabled(False);

    def switch2(self):
        #base arduino
        print("Base movement and lights on")
        ser1.flushInput()
        ser1.flushOutput()
        ser1.write(bytes(b'C1\n'))
        ser1.write(bytes(b'C1\n'))

    def switch3(self):
        # right hand arduino
        print("Hi")
        self.p = subprocess.Popen(["python3", "/home/inker/PycharmProjects/speechmain/start_speak.py"])
        self.t = sleep(5)
        ser3.flushInput()
        ser3.flushOutput()
        ser3.write(bytes(b'C1\n'))
        ser3.write(bytes(b'C1\n'))

    def handle_data(self, data):
        # print(data)
        if (data.find("Completed1") >= 0):
            print(data)
            self.switch2()
        elif (data.find("Completed2") >= 0):
            print(data)
            self.switch3()
        else:
            print(data)
            self.start.setEnabled(True);
            self.t = sleep(1)
            self.start_sig.emit('1')
            self.close()

    def read_from_port(self, ser):
        while True:
            reading = ser.readline().decode()
            self.handle_data(reading)


