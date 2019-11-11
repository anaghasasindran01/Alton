#!/usr/bin/python3
import serial
ser1 = serial.Serial("/dev/ttyACM0",9600, writeTimeout = 0) # base arduino
#ser2 = serial.Serial("/dev/ttyACM0",9600, writeTimeout = 0) # head ardino and led
#ser3 = serial.Serial("/dev/ttyACM1",9600, writeTimeout = 0) # right hand arduino
#ser4 = serial.Serial("/dev/ttyACM2",9600, writeTimeout = 0) # left hand arduino