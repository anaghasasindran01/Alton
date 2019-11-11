from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import signal
import threading
from threading import Timer
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

class testWindow(QtWidgets.QWidget):

    home_sig = QtCore.pyqtSignal(str)
    automatic_sig = QtCore.pyqtSignal(str)
    manual_sig = QtCore.pyqtSignal(str)



    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('test window')
        self.setFixedSize(640, 480)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet("background-image:url(:test/Test bg.jpg)")

        self.automatic = QtWidgets.QPushButton(self)
        self.automatic.setObjectName("Automatic_Test")
        #self.automatic.setText("Automatic Test")
        self.automatic.setGeometry(QtCore.QRect(140, 70, 160, 160))
        self.automatic.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/test/Test A.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.manual = QtWidgets.QPushButton(self)
        self.manual.setObjectName("Manual_Test")
        #self.manual.setText("Manual Test")
        self.manual.setGeometry(QtCore.QRect(340, 70, 160, 160))
        self.manual.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/test/Test M.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.home = QtWidgets.QPushButton(self)
        self.home.setObjectName("close")
        #self.home.setText("Home")
        self.home.setGeometry(QtCore.QRect(0, 0, 50, 480))
        self.home.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.wander = QtWidgets.QFrame(self)
        self.wander.setGeometry(QtCore.QRect(50, 330, 90, 90))
        self.wander.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wander.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wander.setObjectName("wander")
        self.wander.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/test/Test wander.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.gesture = QtWidgets.QFrame(self)
        self.gesture.setGeometry(QtCore.QRect(190, 330, 90, 90))
        self.gesture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gesture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gesture.setObjectName("gesture")
        self.gesture.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/test/Test gesture.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.test = QtWidgets.QFrame(self)
        self.test.setGeometry(QtCore.QRect(330, 310, 130, 130))
        self.test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test.setObjectName("test")
        self.test.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/test/Test test.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.custom = QtWidgets.QFrame(self)
        self.custom.setGeometry(QtCore.QRect(510, 330, 90, 90))
        self.custom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.custom.setObjectName("custom")
        self.custom.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/test/Test cm.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.automatic.clicked.connect(self.switch1)
        self.manual.clicked.connect(self.switch2)
        self.home.clicked.connect(self.switch3)

    def switch1(self):
        self.automatic_sig.emit('1')
        self.close()

    def switch2(self):
        self.manual_sig.emit('1')
        self.close()

    def switch3(self):
        self.home_sig.emit('1')
        self.close()


class automaticWindow(QtWidgets.QWidget):

    back_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)


    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Automatic Test window')
        self.setFixedSize(640, 480)

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/ttest/ttest  bg.jpg)")

        self.test = QtWidgets.QPushButton(self)
        self.test.setGeometry(QtCore.QRect(245, 130, 150, 150))
        #self.test.setText("Test")
        self.test.setObjectName("Test")
        self.test.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/ttest/ttest.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")


        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 0, 50, 480))
        #self.back.setText("BACK")
        self.back.setObjectName("BACK")
        self.back.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.home = QtWidgets.QPushButton(self)
        self.home.setGeometry(QtCore.QRect(590, 0, 50, 480))
        #self.home.setText("HOME")
        self.home.setObjectName("HOME")
        self.home.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.test.clicked.connect(self.switch1)
        self.home.clicked.connect(self.switch5)
        self.back.clicked.connect(self.switch6)

        self.serial_read_thread1 = threading.Thread(target=self.read_from_port, args=(ser_Base,))
        self.serial_read_thread1.start()
        self.serial_read_thread2 = threading.Thread(target=self.read_from_port, args=(ser_Head,))
        self.serial_read_thread2.start()
        self.serial_read_thread3 = threading.Thread(target=self.read_from_port, args=(ser_RHand,))
        self.serial_read_thread3.start()
        self.serial_read_thread4 = threading.Thread(target=self.read_from_port, args=(ser_LHand,))
        self.serial_read_thread4.start()



    def switch1(self):
        print("Testing Started")
        print("Base testing")
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B3\n'))
        ser_Base.write(bytes(b'B3\n'))
        self.test.setEnabled(False);

    def switch2(self):

        print("Right Arm Testing")
        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R3\n'))
        ser_RHand.write(bytes(b'R3\n'))

    def switch3(self):

        print("Left Arm Testing")
        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L3\n'))
        ser_LHand.write(bytes(b'L3\n'))

    def switch4(self):

        print("Head Testing")
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H3\n'))
        ser_Head.write(bytes(b'H3\n'))

    def handle_data(self,data):
        #print(data)
        if (data.find("Success1")>=0):
            print(data)
            self.switch2()
        elif (data.find("Success2")>=0):
            print(data)
            self.switch3()
        elif (data.find("Success3")>=0):
            print(data)
            self.switch4()
            self.test.setEnabled(True);

    def read_from_port(self,ser):
        while True:
           reading = ser.readline().decode()
           self.handle_data(reading)


    def switch5(self):
        self.home_sig.emit('1')
        self.close()
    def switch6(self):
        self.back_sig.emit('1')
        self.close()

class manualWindow(QtWidgets.QWidget):

    back_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)


    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Manual Test window')
        self.setFixedSize(640, 480)
        self.p = 0
        self.t = 0

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/ttest/tbg.jpg)")


        self.base = QtWidgets.QPushButton(self)
        self.base.setGeometry(QtCore.QRect(50, 90, 120, 120))
        #self.base.setText("Base")
        self.base.setObjectName("Base")
        self.base.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/ttest/tBase.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.leftarm = QtWidgets.QPushButton(self)
        self.leftarm.setGeometry(QtCore.QRect(190, 90, 120, 120))
        #self.leftarm.setText("Left Arm")
        self.leftarm.setObjectName("Left_Arm")
        self.leftarm.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/ttest/tLeft Arm.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.rightarm = QtWidgets.QPushButton(self)
        self.rightarm.setGeometry(QtCore.QRect(330, 90, 120, 120))
        #self.rightarm.setText("Right Arm")
        self.rightarm.setObjectName("Right_Arm")
        self.rightarm.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/ttest/tRight Arm.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.head = QtWidgets.QPushButton(self)
        self.head.setGeometry(QtCore.QRect(470, 90, 120, 120))
        #self.head.setText("Head")
        self.head.setObjectName("Head")
        self.head.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/ttest/tHead.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 0, 50, 480))
       # self.back.setText("BACK")
        self.back.setObjectName("BACK")
        self.back.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.home = QtWidgets.QPushButton(self)
        self.home.setGeometry(QtCore.QRect(590, 0, 50, 480))
        #self.home.setText("HOME")
        self.home.setObjectName("HOME")
        self.home.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.base.clicked.connect(self.switch1)
        self.leftarm.clicked.connect(self.switch2)
        self.rightarm.clicked.connect(self.switch3)
        self.head.clicked.connect(self.switch4)
        self.home.clicked.connect(self.switch5)
        self.back.clicked.connect(self.switch6)

        self.serial_read_thread1 = threading.Thread(target=self.read_from_port, args=(ser_Base,))
        self.serial_read_thread1.start()
        self.serial_read_thread2 = threading.Thread(target=self.read_from_port, args=(ser_Head,))
        self.serial_read_thread2.start()
        self.serial_read_thread3 = threading.Thread(target=self.read_from_port, args=(ser_RHand,))
        self.serial_read_thread3.start()
        self.serial_read_thread4 = threading.Thread(target=self.read_from_port, args=(ser_LHand,))
        self.serial_read_thread4.start()

    def switch1(self):
        print("Base Testing")
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B4\n'))
        ser_Base.write(bytes(b'B4\n'))
        self.base.setEnabled(False);

    def switch2(self):
        print("Left Arm Testing")
        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L4\n'))
        ser_LHand.write(bytes(b'L4\n'))
        self.leftarm.setEnabled(False);

    def switch3(self):
        print("Right Arm Testing")
        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R4\n'))
        ser_RHand.write(bytes(b'R4\n'))
        self.rightarm.setEnabled(False);

    def switch4(self):
        print("Head Testing")
        print("Talk to me")
        print("Starting subprocess")
        print("PID-SELF  :", os.getpid())
        #self.p = subprocess.Popen(["python3", "/home/inker/PycharmProjects/speechmain/headtest_speak.py"])
        self.t = sleep(3)
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H4\n'))
        ser_Head.write(bytes(b'H4\n'))
        self.head.setEnabled(False);



    def switch5(self):
        self.home_sig.emit('1')
        self.close()
    def switch6(self):
        self.back_sig.emit('1')
        self.close()

    def read_from_port(self,ser):
        while True:
           reading = ser.readline().decode()
           self.handle_data(reading)


    def handle_data(self,data):
        if (data.find("Completed1")>=0):
            print(data)
            self.base.setEnabled(True);
        elif (data.find("Completed2")>=0):
            print(data)
            self.head.setEnabled(True);
        elif (data.find("Completed3")>=0):
            print(data)
            self.leftarm.setEnabled(True);
        elif (data.find("Completed4")>=0):
            print(data)
            self.rightarm.setEnabled(True);





