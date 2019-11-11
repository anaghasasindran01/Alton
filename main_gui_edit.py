#!/usr/bin/python3


# import serial
from portfix_edit import identify_modules, serial_ports, module_list
import sys
from PyQt5 import QtCore, QtWidgets



#path directory  file
sys.path.insert(0, 'UI')
sys.path.insert(1, 'window')

identify_modules()


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


# ser1 = serial.Serial("/dev/ttyACM0",9600, writeTimeout = 0) # base arduino
#ser2 = serial.Serial("/dev/ttyACM0",9600, writeTimeout = 0) # head ardino and led
#ser3 = serial.Serial("/dev/ttyACM1",9600, writeTimeout = 0) # right hand arduino
#ser4 = serial.Serial("/dev/ttyACM2",9600, writeTimeout = 0) # left hand arduino


#from startwindow import startWindow
#from mainwindow import mainwindow, settingwindow
from homewindow import homewindow,  wanderWindow
from gesturewindow import gestureWindow, imagetrackWindow, voiceWindow, shakehandWindow
from testwindow import testWindow, automaticWindow, manualWindow
from customwindow import customWindow, headWindow, LhandWindow, RhandWindow, baseWindow
from port import*






class Controller:

    def __init__(self):
        pass

    def show_main(self):
        self.window = mainwindow()
        self.window.menu_sig.connect(self.show_homewindow)
        self.window.setting_sig.connect(self.show_settingwindow)
        self.window.show()



    def show_settingwindow(self, text):
        self.window = settingwindow(text)
        self.window.show()
        self.window.back_sig.connect(self.show_main)

    def show_homewindow(self):
        self.window = homewindow()
        self.window.show()
        self.window.wander_sig.connect(self.show_wanderwindow)
        self.window.gesture_sig.connect(self.show_gesturewindow)
        self.window.test_sig.connect(self.show_testwindow)
        self.window.custom_sig.connect(self.show_customwindow)
        self.window.back_sig.connect(self.show_main)

    def show_wanderwindow(self, text):
        self.window = wanderWindow(text)
        self.window.show()
        self.window.back_sig.connect(self.show_homewindow)

    def show_gesturewindow(self, text):
        self.window = gestureWindow(text)
        self.window.show()
        self.window.imagetrack_sig.connect(self.show_imagetrackwindow)
        self.window.speech_sig.connect(self.show_voicewindow)
        self.window.handshake_sig.connect(self.show_shakehandwindow)
        self.window.back_sig.connect(self.show_homewindow)

    def show_imagetrackwindow(self):
        self.window = imagetrackWindow()
        self.window.show()
        self.window.back_sig.connect(self.show_gesturewindow)
        self.window.home_sig.connect(self.show_homewindow)

    def show_voicewindow(self, text):
        self.window = voiceWindow(text)
        self.window.show()
        self.window.back_sig.connect(self.show_gesturewindow)
        self.window.home_sig.connect(self.show_homewindow)


    def show_shakehandwindow(self, text):
        self.window = shakehandWindow(text)
        self.window.show()
        self.window.back_sig.connect(self.show_gesturewindow)
        self.window.home_sig.connect(self.show_homewindow)


    def show_testwindow(self, text):
        self.window = testWindow(text)
        self.window.show()
        self.window.automatic_sig.connect(self.show_automaticwindow)
        self.window.manual_sig.connect(self.show_manualwindow)
        self.window.home_sig.connect(self.show_homewindow)

    def show_automaticwindow(self, text):
        self.window = automaticWindow(text)
        self.window.show()
        self.window.back_sig.connect(self.show_testwindow)
        self.window.home_sig.connect(self.show_homewindow)

    def show_manualwindow(self, text):
        self.window = manualWindow(text)
        self.window.show()
        self.window.back_sig.connect(self.show_testwindow)
        self.window.home_sig.connect(self.show_homewindow)

    def show_customwindow(self, text):
        self.window = customWindow(text)
        self.window.show()
        self.window.head_sig.connect(self.show_headwindow)
        self.window.hand_sig.connect(self.show_Lhandwindow)
        self.window.base_sig.connect(self.show_basewindow)
        self.window.home_sig.connect(self.show_homewindow)

    def show_headwindow(self, text):
        self.window = headWindow(text)
        self.window.show()
        self.window.home_sig.connect(self.show_homewindow)
        self.window.back_sig.connect(self.show_customwindow)

    def show_Lhandwindow(self, text):
        self.window = LhandWindow(text)
        self.window.show()
        self.window.Rhand_sig.connect(self.show_Rhandwindow)
        self.window.home_sig.connect(self.show_homewindow)
        self.window.back_sig.connect(self.show_customwindow)


    def show_Rhandwindow(self, text):
        self.window = RhandWindow(text)
        self.window.show()
        self.window.Lhand_sig.connect(self.show_Lhandwindow)
        self.window.home_sig.connect(self.show_homewindow)
        self.window.back_sig.connect(self.show_customwindow)

    def show_basewindow(self, text):
        self.window = baseWindow(text)
        self.window.show()
        self.window.home_sig.connect(self.show_homewindow)
        self.window.back_sig.connect(self.show_customwindow)


    def show_window_test(self, text):
        self.window_two = Windowtest(text)
        self.window.close()
        self.window_two.show()




import resours

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_homewindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
