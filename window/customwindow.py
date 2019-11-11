from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import (QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt
import os
import subprocess
import signal
import serial
import time
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


class customWindow(QtWidgets.QWidget):

    head_sig = QtCore.pyqtSignal(str)
    hand_sig = QtCore.pyqtSignal(str)
    base_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)



    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('custom window')
        self.setFixedSize(640, 480)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet("background-image:url(:/custom/custom mode BG.jpg)")


        self.head = QtWidgets.QPushButton(self)
        self.head.setObjectName("HEAD")
        #self.head.setText("HEAD")
        self.head.setGeometry(QtCore.QRect(60, 70, 160, 160))
        self.head.setStyleSheet("background-color:transparent;\n"
                                     "border-image:url(:/custom/head.png);\n"
                                     "background: none;\n"
                                     "border: none; border: none; background-repeat: none;")

        self.hand = QtWidgets.QPushButton(self)
        self.hand.setObjectName("HAND")
        #self.hand.setText("HAND")
        self.hand.setGeometry(QtCore.QRect(240, 70, 160, 160))
        self.hand.setStyleSheet("background-color:transparent;\n"
                                     "border-image:url(:/custom/arm.png);\n"
                                     "background: none;\n"
                                     "border: none; border: none; background-repeat: none;")

        self.base = QtWidgets.QPushButton(self)
        self.base.setObjectName("BASE")
        #self.base.setText("BASE")
        self.base.setGeometry(QtCore.QRect(420, 70, 160, 160))
        self.base.setStyleSheet("background-color:transparent;\n"
                                     "border-image:url(:/custom/base.png);\n"
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
                                     "border-image:url(:/custom/cuswander.png);\n"
                                     "background: none;\n"
                                     "border: none; border: none; background-repeat: none;")

        self.gesture = QtWidgets.QFrame(self)
        self.gesture.setGeometry(QtCore.QRect(190, 330, 90, 90))
        self.gesture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gesture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gesture.setObjectName("gesture")
        self.gesture.setStyleSheet("background-color:transparent;\n"
                                     "border-image:url(:/custom/cusgesture.png);\n"
                                     "background: none;\n"
                                     "border: none; border: none; background-repeat: none;")


        self.test = QtWidgets.QFrame(self)
        self.test.setGeometry(QtCore.QRect(330, 330, 90, 90))
        self.test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test.setObjectName("test")
        self.test.setStyleSheet("background-color:transparent;\n"
                                     "border-image:url(:/custom/custest.png);\n"
                                     "background: none;\n"
                                     "border: none; border: none; background-repeat: none;")


        self.custom = QtWidgets.QFrame(self)
        self.custom.setGeometry(QtCore.QRect(470, 310, 130, 130))
        self.custom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.custom.setObjectName("custom")
        self.custom.setStyleSheet("background-color:transparent;\n"
                                     "border-image:url(:/custom/custom mode.png);\n"
                                     "background: none;\n"
                                     "border: none; border: none; background-repeat: none;")


        self.head.clicked.connect(self.switch1)
        self.hand.clicked.connect(self.switch2)
        self.base.clicked.connect(self.switch3)
        self.home.clicked.connect(self.switch4)

    def switch1(self):
        self.head_sig.emit('1')
        self.close()

    def switch2(self):
        self.hand_sig.emit('1')
        self.close()

    def switch3(self):
        self.base_sig.emit('1')
        self.close()

    def switch4(self):
        self.home_sig.emit('1')
        self.close()



class headWindow(QtWidgets.QWidget):

    back_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)


    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Head window')
        self.setFixedSize(640, 480)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet("background-image:url(:/menu/menubg.jpg)")

        self.left = QtWidgets.QPushButton(self)
        self.left.setGeometry(QtCore.QRect(200, 170, 80, 80))
        #self.left.setText("Left")
        self.left.setObjectName("Left")
        self.left.setStyleSheet("background-color:transparent;\n"
                                     "border-image:url(:/arrow/hleft.png);\n"
                                     "background: none;\n"
                                     "border: none; border: none; background-repeat: none;")

        self.right = QtWidgets.QPushButton(self)
        self.right.setGeometry(QtCore.QRect(360, 170, 80, 80))
        #self.right.setText("Right")
        self.right.setObjectName("Right")
        self.right.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/arrow/hright.png);\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.up = QtWidgets.QPushButton(self)
        self.up.setGeometry(QtCore.QRect(280, 90, 80, 80))
        #self.up.setText("up")
        self.up.setObjectName("up")
        self.up.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/arrow/hforward.png);\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.down = QtWidgets.QPushButton(self)
        self.down.setGeometry(QtCore.QRect(280, 250, 80, 80))
        #self.down.setText("down")
        self.down.setObjectName("down")
        self.down.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/arrow/hback.png);\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.straight = QtWidgets.QPushButton(self)
        self.straight.setGeometry(QtCore.QRect(290, 180, 60, 60))
        #self.straight.setText("straight")
        self.straight.setObjectName("straight")
        self.straight.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/arrow/hstop.png);\n"
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

        self.right.pressed.connect(self.switch1)
        self.left.pressed.connect(self.switch2)
        self.down.pressed.connect(self.switch3)
        self.up.pressed.connect(self.switch4)
        self.straight.clicked.connect(self.switch5)
        self.left.released.connect(self.switch0)
        self.right.released.connect(self.switch0)
        self.up.released.connect(self.switch0)
        self.down.released.connect(self.switch0)
        self.home.clicked.connect(self.switch6)
        self.back.clicked.connect(self.switch7)



    def switch0(self):
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H0\n'))
        ser_Head.write(bytes(b'H0\n'))

    def switch1(self):
        print("Right button clicked")
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H5\n'))
        ser_Head.write(bytes(b'H5\n'))

    def switch2(self):
        print("Left button clicked")
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H6\n'))
        ser_Head.write(bytes(b'H6\n'))

    def switch3(self):
        print("Down button clicked")
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H7\n'))
        ser_Head.write(bytes(b'H7\n'))

    def switch4(self):
        print("Up button clicked")
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H8\n'))
        ser_Head.write(bytes(b'H8\n'))

    def switch5(self):
        print("Straight button clicked")
        ser_Head.flushInput()
        ser_Head.flushOutput()
        ser_Head.write(bytes(b'H9\n'))
        ser_Head.write(bytes(b'H9\n'))

    def switch6(self):
        self.home_sig.emit('1')
        self.close()
    def switch7(self):
        self.back_sig.emit('1')
        self.close()





class LhandWindow(QtWidgets.QWidget):

    Rhand_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)
    back_sig = QtCore.pyqtSignal(str)


    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Left hand')
        self.setFixedSize(640, 480)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet("background-image:url(:/ttest/tbg.jpg)")

        self.shoulder_x_slide = QtWidgets.QSlider(self)
        self.shoulder_x_slide.setGeometry(QtCore.QRect(70, 70, 250, 20))
        self.shoulder_x_slide.setOrientation(QtCore.Qt.Horizontal)
        self.shoulder_x_slide.setMinimum(1)
        self.shoulder_x_slide.setMaximum(179)
        self.shoulder_x_slide.setValue(1)
        self.shoulder_x_slide.setTickInterval(5)
        self.shoulder_x_slide.setObjectName("shoulder_x_slide")

        self.shoulder_y_slide = QtWidgets.QSlider(self)
        self.shoulder_y_slide.setGeometry(QtCore.QRect(70, 100, 250, 20))
        self.shoulder_y_slide.setOrientation(QtCore.Qt.Horizontal)
        self.shoulder_y_slide.setMinimum(1)
        self.shoulder_y_slide.setMaximum(179)
        self.shoulder_y_slide.setValue(1)
        self.shoulder_y_slide.setTickInterval(5)
        self.shoulder_y_slide.setObjectName("shoulder_y_slide")

        self.elbow_x_slide = QtWidgets.QSlider(self)
        self.elbow_x_slide.setGeometry(QtCore.QRect(70, 150, 250, 20))
        self.elbow_x_slide.setOrientation(QtCore.Qt.Horizontal)
        self.elbow_x_slide.setMinimum(1)
        self.elbow_x_slide.setMaximum(179)
        self.elbow_x_slide.setValue(90)
        self.elbow_x_slide.setTickInterval(5)
        self.elbow_x_slide.setObjectName("elbow_x_slide")

        self.elbow_y_slide = QtWidgets.QSlider(self)
        self.elbow_y_slide.setGeometry(QtCore.QRect(70, 180, 250, 20))
        self.elbow_y_slide.setOrientation(QtCore.Qt.Horizontal)
        self.elbow_y_slide.setMinimum(1)
        self.elbow_y_slide.setMaximum(179)
        self.elbow_y_slide.setValue(90)
        self.elbow_y_slide.setTickInterval(5)
        self.elbow_y_slide.setObjectName("elbow_y_slide")

        self.wrist_x_slide = QtWidgets.QSlider(self)
        self.wrist_x_slide.setGeometry(QtCore.QRect(70, 230, 250, 20))
        self.wrist_x_slide.setOrientation(QtCore.Qt.Horizontal)
        self.wrist_x_slide.setMinimum(1)
        self.wrist_x_slide.setMaximum(179)
        self.wrist_x_slide.setValue(110)
        self.wrist_x_slide.setTickInterval(5)
        self.wrist_x_slide.setObjectName("wrist_x_slide")

        self.gripper_on = QtWidgets.QPushButton(self)
        self.gripper_on.setGeometry(QtCore.QRect(70, 260, 115, 50))
        self.gripper_on.setText("Gripper ON")
        self.gripper_on.setObjectName("Gripperon")

        self.gripper_off = QtWidgets.QPushButton(self)
        self.gripper_off.setGeometry(QtCore.QRect(210, 260, 115, 50))
        self.gripper_off.setText("Gripper OFF")
        self.gripper_off.setObjectName("Gripperoff")


        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(280, 400, 80, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.right_arm = QtWidgets.QPushButton(self)
        self.right_arm.setGeometry(QtCore.QRect(400, 400, 80, 50))
        self.right_arm.setText("Right")
        self.right_arm.setObjectName("Right arm")

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

        '''v_box = QVBoxLayout()
        self.le.setGeometry(350, 400, 80, 50)
        v_box.addWidget(self.le)
        self.setLayout(v_box)
        self.show()'''

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(360, 55, 80, 50))
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(360, 85, 80, 50))
        self.label2.setObjectName("label2")

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(360, 135, 80, 50))
        self.label3.setObjectName("label3")

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setGeometry(QtCore.QRect(360, 170, 80, 50))
        self.label4.setObjectName("label4")

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setGeometry(QtCore.QRect(360, 215, 80, 50))
        self.label5.setObjectName("label5")

        self.shoulder_x_slide.valueChanged['int'].connect(self.label1.setNum)
        self.shoulder_y_slide.valueChanged['int'].connect(self.label2.setNum)
        self.elbow_x_slide.valueChanged['int'].connect(self.label3.setNum)
        self.elbow_y_slide.valueChanged['int'].connect(self.label4.setNum)
        self.wrist_x_slide.valueChanged['int'].connect(self.label5.setNum)

123456
self.shoulder_x_slide.valueChanged.connect(self.switch4)
        self.shoulder_y_slide.valueChanged.connect(self.switch5)
        self.elbow_x_slide.valueChanged.connect(self.switch6)
        self.elbow_y_slide.valueChanged.connect(self.switch7)
        self.wrist_x_slide.valueChanged.connect(self.switch8)
        self.gripper_on.clicked.connect(self.switch9)
        self.gripper_off.clicked.connect(self.switch10)

        self.right_arm.clicked.connect(self.switch1)
        self.home.clicked.connect(self.switch2)
        self.back.clicked.connect(self.switch3)


    def switch4(self, value):
        print("shoulder x motor")

        value = str(self.shoulder_x_slide.value())
        print(value)

        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L5\n'))
        ser_LHand.write(bytes(b'L5\n'))

        data = "A{}\n".format(value)
        print("output = '" + data + "'")
        ser_LHand.write(data.encode())

    def switch5(self, value):
        print("shoulder y motor")

        value = str(self.shoulder_y_slide.value())
        print(value)

        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L6\n'))
        ser_LHand.write(bytes(b'L6\n'))

        data = "B{}\n".format(value)
        print("output = '" + data + "'")
        ser_LHand.write(data.encode())

    def switch6(self, value):
        print("knee x motor")

        value = str(self.elbow_x_slide.value())
        print(value)

        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L7\n'))
        ser_LHand.write(bytes(b'L7\n'))

        data = "C{}\n".format(value)
        print("output = '" + data + "'")
        ser_LHand.write(data.encode())

    def switch7(self, value):
        print("knee Y motor")

        value = str(self.elbow_y_slide.value())
        print(value)

        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L8\n'))
        ser_LHand.write(bytes(b'L8\n'))

        data = "D{}\n".format(value)
        print("output = '" + data + "'")
        ser_LHand.write(data.encode())

    def switch8(self, value):
        print("wrist x motor")

        value = str(self.wrist_x_slide.value())
        print(value)

        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L9\n'))
        ser_LHand.write(bytes(b'L9\n'))

        data = "E{}\n".format(value)
        print("output = '" + data + "'")
        ser_LHand.write(data.encode())

    def switch9(self):
        print("gripper on button clicked")
        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L10\n'))
        ser_LHand.write(bytes(b'L10\n'))

    def switch10(self):
        print("gripper off button clicked")
        ser_LHand.flushInput()
        ser_LHand.flushOutput()
        ser_LHand.write(bytes(b'L11\n'))
        ser_LHand.write(bytes(b'L11\n'))

    def switch1(self):
        self.Rhand_sig.emit('1')
        self.close()

    def switch2(self):
        self.home_sig.emit('1')
        self.close()

    def switch3(self):
        self.back_sig.emit('1')
        self.close()





class RhandWindow(QtWidgets.QWidget):

    Lhand_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)
    back_sig = QtCore.pyqtSignal(str)

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Right hand')
        self.setFixedSize(640, 480)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet("background-image:url(:/gesture/Gesture bg.jpg)")

        self.shoulder_x_slide = QtWidgets.QSlider(self)
        self.shoulder_x_slide.setGeometry(QtCore.QRect(70, 70, 250, 20))
        self.shoulder_x_slide.setOrientation(QtCore.Qt.Horizontal)
        self.shoulder_x_slide.setMinimum(1)
        self.shoulder_x_slide.setMaximum(179)
        self.shoulder_x_slide.setValue(179)
        self.shoulder_x_slide.setTickInterval(5)
        self.shoulder_x_slide.setObjectName("shoulder_x_slide")

        self.shoulder_y_slide = QtWidgets.QSlider(self)
        self.shoulder_y_slide.setGeometry(QtCore.QRect(70, 100, 250, 20))
        self.shoulder_y_slide.setOrientation(QtCore.Qt.Horizontal)
        self.shoulder_y_slide.setMinimum(1)
        self.shoulder_y_slide.setMaximum(179)
        self.shoulder_y_slide.setValue(1)
        self.shoulder_y_slide.setTickInterval(5)
        self.shoulder_y_slide.setObjectName("shoulder_y_slide")

        self.elbow_x_slide = QtWidgets.QSlider(self)
        self.elbow_x_slide.setGeometry(QtCore.QRect(70, 150, 250, 20))
        self.elbow_x_slide.setOrientation(QtCore.Qt.Horizontal)
        self.elbow_x_slide.setMinimum(1)
        self.elbow_x_slide.setMaximum(179)
        self.elbow_x_slide.setValue(90)
        self.elbow_x_slide.setTickInterval(5)
        self.elbow_x_slide.setObjectName("elbow_x_slide")

        self.elbow_y_slide = QtWidgets.QSlider(self)
        self.elbow_y_slide.setGeometry(QtCore.QRect(70, 180, 250, 20))
        self.elbow_y_slide.setOrientation(QtCore.Qt.Horizontal)
        self.elbow_y_slide.setMinimum(1)
        self.elbow_y_slide.setMaximum(179)
        self.elbow_y_slide.setValue(90)
        self.elbow_y_slide.setTickInterval(5)
        self.elbow_y_slide.setObjectName("elbow_y_slide")

        self.wrist_x_slide = QtWidgets.QSlider(self)
        self.wrist_x_slide.setGeometry(QtCore.QRect(70, 230, 250, 20))
        self.wrist_x_slide.setOrientation(QtCore.Qt.Horizontal)
        self.wrist_x_slide.setMinimum(1)
        self.wrist_x_slide.setMaximum(179)
        self.wrist_x_slide.setValue(90)
        self.wrist_x_slide.setTickInterval(5)
        self.wrist_x_slide.setObjectName("wrist_x_slide")

        self.gripper_on = QtWidgets.QPushButton(self)
        self.gripper_on.setGeometry(QtCore.QRect(70, 260, 115, 50))
        self.gripper_on.setText("Gripper ON")
        self.gripper_on.setObjectName("Gripperon")

        self.gripper_off = QtWidgets.QPushButton(self)
        self.gripper_off.setGeometry(QtCore.QRect(210, 260, 115, 50))
        self.gripper_off.setText("Gripper OFF")
        self.gripper_off.setObjectName("Gripperoff")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(400, 400, 80, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.left_arm = QtWidgets.QPushButton(self)
        self.left_arm.setGeometry(QtCore.QRect(280, 400, 80, 50))
        self.left_arm.setText("Left")
        self.left_arm.setObjectName("Left arm")

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

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(360, 55, 80, 50))
        self.label1.setObjectName("label1")

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(360, 85, 80, 50))
        self.label2.setObjectName("label2")

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(360, 135, 80, 50))
        self.label3.setObjectName("label3")

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setGeometry(QtCore.QRect(360, 170, 80, 50))
        self.label4.setObjectName("label4")

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setGeometry(QtCore.QRect(360, 215, 80, 50))
        self.label5.setObjectName("label5")

        self.shoulder_x_slide.valueChanged['int'].connect(self.label1.setNum)
        self.shoulder_y_slide.valueChanged['int'].connect(self.label2.setNum)
        self.elbow_x_slide.valueChanged['int'].connect(self.label3.setNum)
        self.elbow_y_slide.valueChanged['int'].connect(self.label4.setNum)
        self.wrist_x_slide.valueChanged['int'].connect(self.label5.setNum)

        self.shoulder_x_slide.valueChanged.connect(self.switch4)
        self.shoulder_y_slide.valueChanged.connect(self.switch5)
        self.elbow_x_slide.valueChanged.connect(self.switch6)
        self.elbow_y_slide.valueChanged.connect(self.switch7)
        self.wrist_x_slide.valueChanged.connect(self.switch8)
        self.gripper_on.clicked.connect(self.switch9)
        self.gripper_off.clicked.connect(self.switch10)

        self.left_arm.clicked.connect(self.switch1)
        self.home.clicked.connect(self.switch2)
        self.back.clicked.connect(self.switch3)

    def switch4(self, value):
        print("shoulder x motor")

        value = str(self.shoulder_x_slide.value())
        print(value)

        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R5\n'))
        ser_RHand.write(bytes(b'R5\n'))

        data = "A{}\n".format(value)
        print("output = '" + data + "'")
        ser_RHand.write(data.encode())

    def switch5(self, value):
        print("shoulder y motor")

        value = str(self.shoulder_y_slide.value())
        print(value)

        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R6\n'))
        ser_RHand.write(bytes(b'R6\n'))

        data = "B{}\n".format(value)
        print("output = '" + data + "'")
        ser_RHand.write(data.encode())

    def switch6(self, value):
        print("knee x motor")

        value = str(self.elbow_x_slide.value())
        print(value)

        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R7\n'))
        ser_RHand.write(bytes(b'R7\n'))

        data = "C{}\n".format(value)
        print("output = '" + data + "'")
        ser_RHand.write(data.encode())

    def switch7(self, value):
        print("knee Y motor")

        value = str(self.elbow_y_slide.value())
        print(value)

        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R8\n'))
        ser_RHand.write(bytes(b'R8\n'))

        data = "D{}\n".format(value)
        print("output = '" + data + "'")
        ser_RHand.write(data.encode())

    def switch8(self, value):
        print("wrist x motor")

        value = str(self.wrist_x_slide.value())
        print(value)

        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R9\n'))
        ser_RHand.write(bytes(b'R9\n'))

        data = "E{}\n".format(value)
        print("output = '" + data + "'")
        ser_RHand.write(data.encode())

    def switch9(self):
        print("grab on button clicked")
        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R10\n'))
        ser_RHand.write(bytes(b'R10\n'))

    def switch10(self):
        print("grab off button clicked")
        ser_RHand.flushInput()
        ser_RHand.flushOutput()
        ser_RHand.write(bytes(b'R11\n'))
        ser_RHand.write(bytes(b'R11\n'))


    def switch1(self):
        self.Lhand_sig.emit('1')
        self.close()

    def switch2(self):
        self.home_sig.emit('1')
        self.close()

    def switch3(self):
        self.back_sig.emit('1')
        self.close()



class baseWindow(QtWidgets.QWidget):

    back_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('base window')
        self.setFixedSize(640, 480)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setStyleSheet("background-image:url(:/ggesture/gvoice.jpg)")


        self.up = QtWidgets.QPushButton(self)
        self.up.setGeometry(QtCore.QRect(150, 90, 80, 80))
        #self.up.setText("forward")
        self.up.setObjectName("forward")
        self.up.setStyleSheet("background-color:transparent;\n"
                              "border-image:url(:/arrow/hforward.png);\n"
                              "background: none;\n"
                              "border: none; border: none; background-repeat: none;")


        self.down = QtWidgets.QPushButton(self)
        self.down.setGeometry(QtCore.QRect(150, 250, 80, 80))
        #self.down.setText("backward")
        self.down.setObjectName("backward")
        self.down.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/arrow/hback.png);\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.left = QtWidgets.QPushButton(self)
        self.left.setGeometry(QtCore.QRect(70, 170, 80, 80))
        #self.left.setText("Left")
        self.left.setObjectName("Left")
        self.left.setStyleSheet("background-color:transparent;\n"
                                "border-image:url(:/arrow/hleft.png);\n"
                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.right = QtWidgets.QPushButton(self)
        self.right.setGeometry(QtCore.QRect(230, 170, 80, 80))
        #self.right.setText("Right")
        self.right.setObjectName("Right")
        self.right.setStyleSheet("background-color:transparent;\n"
                                 "border-image:url(:/arrow/hright.png);\n"
                                 "background: none;\n"
                                 "border: none; border: none; background-repeat: none;")

        self.stop = QtWidgets.QPushButton(self)
        self.stop.setGeometry(QtCore.QRect(160, 180, 60, 60))
        #self.stop.setText("stop")
        self.stop.setObjectName("stop")
        self.stop.setStyleSheet("background-color:transparent;\n"
                                    "border-image:url(:/arrow/hstop.png);\n"
                                    "background: none;\n"
                                    "border: none; border: none; background-repeat: none;")

        self.R_slider = QtWidgets.QSlider(self)
        self.R_slider.setGeometry(QtCore.QRect(330, 110, 250, 30))
        self.R_slider.setMaximum(255)
        self.R_slider.setOrientation(QtCore.Qt.Horizontal)
        self.R_slider.setObjectName("Red slider")


        self.G_slider = QtWidgets.QSlider(self)
        self.G_slider.setGeometry(QtCore.QRect(330, 180, 250, 30))
        self.G_slider.setMaximum(255)
        self.G_slider.setOrientation(QtCore.Qt.Horizontal)
        self.G_slider.setObjectName("Green slider")

        self.B_slider = QtWidgets.QSlider(self)
        self.B_slider.setGeometry(QtCore.QRect(330, 250, 250, 30))
        self.B_slider.setMaximum(255)
        self.B_slider.setOrientation(QtCore.Qt.Horizontal)
        self.B_slider.setObjectName("Blue slider")

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

        self.left.clicked.connect(self.switch1)
        self.right.clicked.connect(self.switch2)
        self.up.clicked.connect(self.switch3)
        self.down.clicked.connect(self.switch4)
        self.stop.clicked.connect(self.switch5)
        self.home.clicked.connect(self.switch6)
        self.back.clicked.connect(self.switch7)
        self.R_slider.valueChanged.connect(self.switch8)
        self.G_slider.valueChanged.connect(self.switch9)
        self.B_slider.valueChanged.connect(self.switch10)



    def switch1(self):
        print("Left button clicked")
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B5\n'))
        ser_Base.write(bytes(b'B5\n'))

    def switch2(self):
        print("Right button clicked")
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B6\n'))
        ser_Base.write(bytes(b'B6\n'))

    def switch3(self):
        print("Forward button clicked")
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B7\n'))
        ser_Base.write(bytes(b'B7\n'))

    def switch4(self):
        print("Backward button clicked")
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B8\n'))
        ser_Base.write(bytes(b'B8\n'))

    def switch5(self):
        print("stop button clicked")
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B0\n'))
        ser_Base.write(bytes(b'B0\n'))

    def switch6(self):
        self.home_sig.emit('1')
        self.close()

    def switch7(self):
        self.back_sig.emit('1')
        self.close()

    def switch8(self, value):
        print(value)
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B9\n'))
        ser_Base.write(bytes(b'B9\n'))

        data = "R{}\n".format(value)
        print("output = '" + data + "'")
        ser_Base.write(data.encode())

    def switch9(self, value):
        print(value)
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B9\n'))
        ser_Base.write(bytes(b'B9\n'))

        data = "G{}\n".format(value)
        print("output = '" + data + "'")
        ser_Base.write(data.encode())

    def switch10(self, value):
        print(value)
        ser_Base.flushInput()
        ser_Base.flushOutput()
        ser_Base.write(bytes(b'B9\n'))
        ser_Base.write(bytes(b'B9\n'))

        data = "L{}\n".format(value)
        print("output = '" + data + "'")
        ser_Base.write(data.encode())












