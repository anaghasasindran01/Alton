from PyQt5 import QtCore, QtGui, QtWidgets
import os
import subprocess
import signal

class mainwindow(QtWidgets.QWidget):


    menu_sig = QtCore.pyqtSignal(str)
    setting_sig = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')
        self.setFixedSize(640, 480)

        self.home = QtWidgets.QFrame(self)
        self.home.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home.setStyleSheet("background-image:url(:/menu/menubg.jpg)")

        self.menu = QtWidgets.QPushButton(self)
        self.menu.setGeometry(QtCore.QRect(170, 170, 140, 140))
        #self.menu.setText("menu")
        self.menu.setObjectName("menu")
        self.menu.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/menu/Menu but.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")


        self.settings = QtWidgets.QPushButton(self)
        self.settings.setGeometry(QtCore.QRect(330, 170, 140, 140))
        #self.settings.setText("setting")
        self.settings.setObjectName("settings")
        self.settings.setStyleSheet("background-color:transparent;\n"
                                  "border-image:url(:/menu/setting but.png);\n"
                                  "background: none;\n"
                                  "border: none; border: none; background-repeat: none;")




        self.menu.clicked.connect(self.switch)
        self.settings.clicked.connect(self.switch1)

    def switch(self):
        self.menu_sig.emit('1')
        self.close()

    def switch1(self):
        self.setting_sig.emit('1')
        self.close()



class settingwindow(QtWidgets.QWidget):

    back_sig = QtCore.pyqtSignal(str)

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('setting window')
        self.setFixedSize(640, 480)

        self.back = QtWidgets.QPushButton(self)
        self.back.setGeometry(QtCore.QRect(0, 240, 60, 50))
        self.back.setText("back")
        self.back.setObjectName("back")

        self.back.clicked.connect(self.switch)

    def switch(self):
        self.back_sig.emit('1')
        self.close()


