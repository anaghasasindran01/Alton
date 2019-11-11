from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import signal
import serial

#from port import*
from port_enumerate import identify_modules, serial_ports, module_list

ser_Head =None
ser_Base =None
ser_RHand =None
ser_LHand =None

# Serial ports can be assigned like this
for index, module in enumerate(module_list):
    if module == 'HEAD':
        ser_Head = serial_ports[index]
    elif module == 'BASE':
        ser_Base = serial_ports[index]
    elif module == 'RHAND':
        ser_RHand = serial_ports[index]
    elif module == 'LHAND':
        ser_LHand = serial_ports[index]


class homewindow(QtWidgets.QWidget):
    wander_sig = QtCore.pyqtSignal(str)
    gesture_sig = QtCore.pyqtSignal(str)
    test_sig = QtCore.pyqtSignal(str)
    custom_sig = QtCore.pyqtSignal(str)
    back_sig = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Home window')
        self.setFixedSize(640, 480)
        # self.setStyleSheet("background-image:url(:/home/homebg.jpg)")

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/home/homebg.jpg)")
        # self.home.setObjectName("wander")

        self.wander = QtWidgets.QPushButton(self)
        self.wander.setGeometry(QtCore.QRect(70, 330, 90, 90))
        self.wander.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/home/home-wander.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")
        # self.wander.setText("wander")
        self.wander.setObjectName("wander")

        self.gesture = QtWidgets.QPushButton(self)
        self.gesture.setGeometry(QtCore.QRect(210, 330, 90, 90))
        # self.gesture.setText("gesture")
        self.gesture.setStyleSheet("background-color:transparent;\n"
                                   "border-image:url(:/home/home-gesture.png);\n"
                                   "background: none;\n"
                                   "border: none; border: none; background-repeat: none;")
        self.gesture.setObjectName("gesture")

        self.test = QtWidgets.QPushButton(self)
        self.test.setGeometry(QtCore.QRect(350, 330, 90, 90))
        # self.test.setText("test")
        self.test.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/home/home-test.png);\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")
        self.test.setObjectName("test")

        self.custom = QtWidgets.QPushButton(self)
        self.custom.setGeometry(QtCore.QRect(490, 330, 90, 90))
        # self.custom.setText("custom")
        self.custom.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/home/home-cm.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")
        self.custom.setObjectName("custom")

        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 0, 50, 480))
        self.back.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")
        self.back.setObjectName("back")

        self.wander.clicked.connect(self.switch1)
        self.gesture.clicked.connect(self.switch2)
        self.test.clicked.connect(self.switch3)
        self.custom.clicked.connect(self.switch4)
        self.back.clicked.connect(self.switch5)

    def switch1(self):
        self.wander_sig.emit('1')
        self.close()

    def switch2(self):
        self.gesture_sig.emit('1')
        self.close()

    def switch3(self):
        self.test_sig.emit('1')
        self.close()

    def switch4(self):
        self.custom_sig.emit('1')
        self.close()

    def switch5(self):
        self.back_sig.emit('1')
        self.close()


class wanderWindow(QtWidgets.QWidget):

    back_sig = QtCore.pyqtSignal(str)

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('wander window')
        self.setFixedSize(640, 480)

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/menu/menubg.jpg)")

        self.start = QtWidgets.QPushButton(self)
        self.start.setObjectName("START")
        #self.start.setText("START")
        self.start.setGeometry(QtCore.QRect(180, 130, 150, 150))
        self.start.clicked.connect(self.switch1)
        self.start.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/wander/wstart.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")

        self.stop = QtWidgets.QPushButton(self)
        self.stop.setObjectName("STOP")
        #self.stop.setText("STOP")
        self.stop.setGeometry(QtCore.QRect(350, 130, 150, 150))
        self.stop.clicked.connect(self.switch2)
        self.stop.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/wander/wstop.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")

        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 0, 50, 480))
        self.back.setObjectName("back")
        self.back.setStyleSheet("background-color:transparent;\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.wander = QtWidgets.QFrame(self)
        self.wander.setGeometry(QtCore.QRect(50, 310, 130, 130))
        self.wander.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wander.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wander.setObjectName("wander")
        self.wander.setStyleSheet("background-color:transparent;\n"
                                   "border-image:url(:/wander/wwander.png);\n"
                                   "background: none;\n"
                                   "border: none; border: none; background-repeat: none;")

        self.gesture = QtWidgets.QFrame(self)
        self.gesture.setGeometry(QtCore.QRect(230, 330, 90, 90))
        self.gesture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gesture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gesture.setObjectName("gesture")
        self.gesture.setStyleSheet("background-color:transparent;\n"
                                   "border-image:url(:/wander/wgesture.png);\n"
                                   "background: none;\n"
                                   "border: none; border: none; background-repeat: none;")

        self.test = QtWidgets.QFrame(self)
        self.test.setGeometry(QtCore.QRect(370, 330, 90, 90))
        self.test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test.setObjectName("test")
        self.test.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/wander/wtest.png);\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.custom = QtWidgets.QFrame(self)
        self.custom.setGeometry(QtCore.QRect(510, 330, 90, 90))
        self.custom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.custom.setObjectName("custom")
        self.custom.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/wander/wcustom.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")

        self.start.clicked.connect(self.switch1)
        self.stop.clicked.connect(self.switch2)
        self.back.clicked.connect(self.switch3)




    def switch1(self):
        print("wander mode started")
        try:
            ser_Head.flushInput()
            ser_Head.flushOutput()
            ser_Head.write(bytes(b'B2\n'))
            ser_Head.write(bytes(b'B2\n'))
        except:
            print("An exception has occurred when coming back to home.Command might not have sent correctly.")
        else:
            print("serial write have worked correctly.Now we can continue.")

    def switch2(self):
        print("wander mode stopped")
        try:
            ser_Head.flushInput()
            ser_Head.flushOutput()
            ser_Head.write(bytes(b'B0\n'))
            ser_Head.write(bytes(b'B0\n'))
        except:
            print("An exception has occurred when sending wandering mode.Command might not have sent properly.")
        else:
            print("serial write has worked correctly.Now we can continue.")

    def switch3(self):
            self.back_sig.emit('1')
            self.close()








