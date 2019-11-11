import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#import pyqtgraph as pg
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

import os
import subprocess
import signal

import serial
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

#ls -ltrh /dev/video*


#import cv2
#from port import*

#ser3 = serial.Serial("/dev/ttyACM1",9600, writeTimeout = 0)#right hand

class gestureWindow(QtWidgets.QWidget):

    imagetrack_sig = QtCore.pyqtSignal(str)
    speech_sig = QtCore.pyqtSignal(str)
    handshake_sig = QtCore.pyqtSignal(str)
    back_sig = QtCore.pyqtSignal(str)



    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('gesture window')
        self.setFixedSize(640, 480)

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/gesture/Gesture bg.jpg)")


        self.image_track = QtWidgets.QPushButton(self)
        self.image_track.setObjectName("TRACK")
        #self.image_track.setText("TRACK")
        self.image_track.setGeometry(QtCore.QRect(60, 70, 160, 160))
        self.image_track.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/gesture/Gesture image T.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")

        self.speech = QtWidgets.QPushButton(self)
        self.speech.setObjectName("SPEECH")
        #self.speech.setText("SPEECH")
        self.speech.setGeometry(QtCore.QRect(240, 70, 160, 160))
        self.speech.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/gesture/Gesture speech.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.hand_shake = QtWidgets.QPushButton(self)
        self.hand_shake.setObjectName("HAND SHAKE")
        #self.hand_shake.setText("HAND SHAKE")
        self.hand_shake.setGeometry(QtCore.QRect(420, 70, 160, 160))
        self.hand_shake.setStyleSheet("background-color:transparent;\n"
                                       "border-image:url(:/gesture/shakehand.png);\n"
                                       "background: none;\n"
                                       "border: none; border: none; background-repeat: none;")

        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 0, 50, 480))
        self.back.setObjectName("back")
        self.back.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.wander = QtWidgets.QFrame(self)
        self.wander.setGeometry(QtCore.QRect(50, 330, 90, 90))
        self.wander.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wander.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wander.setObjectName("wander")
        self.wander.setStyleSheet("background-color:transparent;\n"
                                      "border-image:url(:/gesture/Gesture wander.png);\n"
                                      "background: none;\n"
                                      "border: none; border: none; background-repeat: none;")

        self.gesture = QtWidgets.QFrame(self)
        self.gesture.setGeometry(QtCore.QRect(190, 310, 130, 130))
        self.gesture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gesture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gesture.setObjectName("gesture")
        self.gesture.setStyleSheet("background-color:transparent;\n"
                                      "border-image:url(:/gesture/Gesture gesture.png);\n"
                                      "background: none;\n"
                                      "border: none; border: none; background-repeat: none;")

        self.test = QtWidgets.QFrame(self)
        self.test.setGeometry(QtCore.QRect(370, 330, 90, 90))
        self.test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test.setObjectName("test")
        self.test.setStyleSheet("background-color:transparent;\n"
                                      "border-image:url(:/gesture/Gesture test.png);\n"
                                      "background: none;\n"
                                      "border: none; border: none; background-repeat: none;")

        self.custom = QtWidgets.QFrame(self)
        self.custom.setGeometry(QtCore.QRect(510, 330, 90, 90))
        self.custom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.custom.setObjectName("custom")
        self.custom.setStyleSheet("background-color:transparent;\n"
                                      "border-image:url(:/gesture/Gesture cm.png);\n"
                                      "background: none;\n"
                                      "border: none; border: none; background-repeat: none;")

        self.image_track.clicked.connect(self.switch1)
        self.speech.clicked.connect(self.switch2)
        self.hand_shake.clicked.connect(self.switch3)
        self.back.clicked.connect(self.switch4)



    def switch1(self):
        self.imagetrack_sig.emit('1')
        self.close()

    def switch2(self):
        self.speech_sig.emit('1')
        self.close()

    def switch3(self):
        self.handshake_sig.emit('1')
        self.close()

    def switch4(self):
        self.back_sig.emit('1')
        self.close()





class imagetrackWindow(QtWidgets.QWidget):


    back_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)

    def __init__(self, camera = None):
        super().__init__()
        self.camera = camera
        
        
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Face track')
        self.setFixedSize(640, 480)

        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setObjectName("image_label")
        self.image_label.setText("image label")
        self.image_label.setGeometry(QtCore.QRect(50, 0, 540, 480))

        
        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 0, 50, 480))
        self.back.setText("BACK")
        self.back.setObjectName("BACK")

        self.start = QtWidgets.QPushButton(self)
        self.start.setGeometry(QtCore.QRect(590, 0, 50, 480))
        self.start.setText("start")
        self.start.setObjectName("start")

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.start.clicked.connect(self.cntrl)

        self.back.clicked.connect(self.switch1)

    

    def switch1(self):
        self.back_sig.emit('1')
        self.close()
        
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.image_label.setPixmap(QPixmap.fromImage(qImg))

    def cntrl(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.start.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.start.setText("Start")


class voiceWindow(QtWidgets.QWidget):


    back_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('voice window')
        self.setFixedSize(640, 480)
        self.p = 0

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/ggesture/gvoice.jpg)")

        self.start = QtWidgets.QPushButton(self)
        self.start.setObjectName("START")
        #self.start.setText("START")
        self.start.setGeometry(QtCore.QRect(180, 130, 150, 150))
        self.start.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/ggesture/gstart.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")

        self.stop = QtWidgets.QPushButton(self)
        self.stop.setObjectName("STOP")
        #self.stop.setText("STOP")
        self.stop.setGeometry(QtCore.QRect(350, 130, 150, 150))
        self.stop.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/ggesture/gstop.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")

        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0,0, 50, 480))
        #self.back.setText("BACK")
        self.back.setObjectName("BACK")
        self.back.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.home = QtWidgets.QPushButton(self)
        self.home.setGeometry(QtCore.QRect(590, 50, 50, 480))
        #self.home.setText("HOME")
        self.home.setObjectName("HOME")
        self.home.setStyleSheet("background-color:transparent;\n"

                                "background: none;\n"
                                "border: none; border: none; background-repeat: none;")

        self.start.clicked.connect(self.switch1)
        self.stop.clicked.connect(self.switch2)
        self.home.clicked.connect(self.switch3)
        self.back.clicked.connect(self.switch4)

    def switch1(self):
        print("Talk to me")
        print("Starting subprocess")
        print("PID-SELF  :", os.getpid())
        #self.p = subprocess.Popen(["python3","/home/inker/PycharmProjects/speechmain/head_speak.py"])
        self.p = subprocess.Popen(["python3", "/home/inker/PycharmProjects/speechmain/speech_fazi/speechv3.py"])

    def switch2(self):
        print("Bye human")
        #Popen.terminate()
        print("Ending subprocess")
        print("PID  :  ", self.p.pid)
        os.kill(self.p.pid, signal.SIGTERM)


    def switch3(self):
        self.home_sig.emit('1')
        self.close()

    def switch4(self):
        self.back_sig.emit('1')
        self.close()


class shakehandWindow(QtWidgets.QWidget):

    back_sig = QtCore.pyqtSignal(str)
    home_sig = QtCore.pyqtSignal(str)

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('shakehand window')
        self.setFixedSize(640, 480)

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/ggesture/gshake.jpg)")


        self.start = QtWidgets.QPushButton(self)
        self.start.setObjectName("START")
        #self.start.setText("START")
        self.start.setGeometry(QtCore.QRect(245, 130, 150, 150))
        self.start.setStyleSheet("background-color:transparent;\n"
                                 "border-image:url(:/ggesture/gstart.png);\n"
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

        self.start.clicked.connect(self.switch1)
        self.home.clicked.connect(self.switch3)
        self.back.clicked.connect(self.switch2)

    def switch1(self):
        print("hand shake mode")
        ser3.flushInput()
        ser3.flushOutput()
        ser3.write(bytes(b'R2\n'))
        ser3.write(bytes(b'R2\n'))

    def switch2(self):
        self.back_sig.emit('1')
        self.close()

    def switch3(self):
        self.home_sig.emit('1')
        self.close()

