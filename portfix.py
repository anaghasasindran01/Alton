#!/usr/bin/python3
import serial
import threading
from subprocess import Popen, check_output, PIPE, CalledProcessError

serial_ports = [None, None]

serial_port_prefixes = ['tnt', 'ttyACM', 'ttyUSB']
module_list = ["BASE", "HEAD"]#, "RHAND", "LHAND"]
module_set_flag_list = [False, False]#, False, False]

serial_ports_list = []
ser_read_thread_list = []
ser_read_thread_active_flag_list = []
ser_open_list = []


def enumerate_serial_ports():
	global serial_ports_list
	err = 0
	try:
		ls_output = Popen(['ls',"/dev"], stdout=PIPE) # running subprocess
		temp_serial_ports = check_output(['grep', '-e', serial_port_prefixes[0], '-e', serial_port_prefixes[1]], stdin=ls_output.stdout).decode('ascii').rstrip() # storing the output to a variable
	except CalledProcessError:
		print("No Serial ports found!!! Check connection...")
		err=1

	else:
		serial_ports_list = temp_serial_ports.split() # identified serial ports will be stored to serial ports list
		if len(serial_ports_list) == 0 :
			print("No Serial ports found!!! Check connection...")
			err=1
			return -1
		else:
			print(serial_ports_list)

	return err

def id_enquiry(ser, ser_read_thread):
	ser_read_thread.start()
	ser.flushInput()
	ser.flushOutput()
	ser.write(bytes(b'?\r\n'))
	ser.write(bytes(b'?\r\n'))

def read_from_port(ser, flag_index):
	global ser_read_thread_active_flag_list
	# print("READING FROM PORT :", flag_index)	
	while ser_read_thread_active_flag_list[flag_index]:
		# print("In loop")
		# print(flag_index, ':',ser_read_thread_active_flag_list[flag_index])
		reading = ser.readline().decode()
		handle_data(reading, ser, flag_index)
	print("Thread exited :", flag_index)


def handle_data(data, ser, flag_index):
	global module_ser_list, module_set_flag_list, ser_read_thread_active_flag_list, serial_ports
	for index, module in enumerate(module_list):
		if (data.find(module)>=0) and ser_read_thread_active_flag_list[flag_index] == True:
			serial_ports[index]=ser
			if module_set_flag_list[index] == False:
				module_set_flag_list[index] = True
			else:
				print('#'*60)
				print('ERROR!!!',module,' ALREADY REGISTERED AT', serial_ports[index].name)
				print('AGAIN FOUND AT',ser.name)
				print('CHECK MODULES....')
			ser_read_thread_active_flag_list[flag_index]=False


def identify_modules():
	global serial_ports_list, ser_read_thread_list, ser_open_list, module_ser_list, ser1, ser_read_thread_active_flag_list
	# global base_set_flag, head_set_flag, rhand_set_flag, lhand_set_flag

	enumerate_serial_ports()
	print("Port List :", serial_ports_list)
	for index, serial_port in enumerate(serial_ports_list):
		print("Serial_port :", serial_port)
		temp_serial = serial.Serial('/dev/'+serial_port,9600, writeTimeout = 0, timeout=1)
		ser_read_thread_active_flag_list.append(True)
		temp_thread = threading.Thread(target=read_from_port, args=(temp_serial, index))
		ser_read_thread_list.append(temp_thread)
		id_enquiry(temp_serial, temp_thread)
		ser_open_list.append(temp_serial)

	print("Started Enquiry...")
	# print(ser_read_thread_list)
	while True:
		if all(item == True for item in module_set_flag_list):
			print("Found all modules...")
			break
	print("ser_read_thread_active_flag_list")
	print(ser_read_thread_active_flag_list)


	for index, flag in enumerate(ser_read_thread_active_flag_list):
		print("Index", index)
		if flag == True:
			print("Closing unwanted serial port :", ser_open_list[index].name, index)
			ser_read_thread_active_flag_list[index] = False
			ser_open_list[index].close()
			print("ser_read_thread_active_flag_list")
			print(ser_read_thread_active_flag_list)
		ser_read_thread_list[index].join()
		print(ser_read_thread_list[index].isAlive())
	print("All threads exited")
	for index, module in enumerate(serial_ports):
		print('Found',module_list[index],'at', module.name)

identify_modules()



