#!/usr/bin/python3
import serial
import threading
from subprocess import Popen, check_output, PIPE, CalledProcessError

# The list of serial ports for the corresponding modules in module_list
serial_ports = [None, None, None, None]


serial_port_prefixes = ['ttyACM','ttyUSB']
module_list = ["BASE", "HEAD", "RHAND", "LHAND"]
module_set_flag_list = [False, False, False, False]

serial_ports_list = []
# The list of all declared threads (for all available serial ports)
ser_read_thread_list = []
# The list of flags to indicate the corresponding thread in ser_read_thread_list is active or not.
ser_read_thread_active_flag_list = []
# The list of opened serial port objects.
ser_open_list = []


def enumerate_serial_ports():
	global serial_ports_list
	err = 0
	try:
		ls_output = Popen(['ls',"/dev"], stdout=PIPE)
		temp_serial_ports = check_output(['grep', '-e', serial_port_prefixes[0], '-e', serial_port_prefixes[1]], stdin=ls_output.stdout).decode('ascii').rstrip()
		print("temporay serial ports are: ",temp_serial_ports)
	except Exception as e:
		print("No Serial ports found!!! Check connection...")
		print("Error !!!", e)
		err=1

	else:
		serial_ports_list = temp_serial_ports.split()
		if len(serial_ports_list) == 0 :
			print("No Serial ports found!!! Check connection...")
			err=1
			return -1
		else:
			# serial_ports_list = [serial_ports_list[0],serial_ports_list[2],serial_ports_list[4],serial_ports_list[6]]
			print("\nAvailable serial ports are :\n",serial_ports_list)

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
		# print(flag_index, ':',ser_read_thread_active_flag_list[flag_index])
		try:
			print("Try to read {}".format(ser.name))
			reading = ser.readline().decode()
		except Exception as e:
			print("ERROR IN READING {}!!!".format(ser.name))
			print(e)
		else:
			print("Successful in reading {}".format(ser.name))
			#print("read data : ", reading)
			handle_data(reading, ser, flag_index)
		ser.flushInput()
		ser.flushOutput()
		ser.write(bytes(b'?\r\n'))
		ser.write(bytes(b'?\r\n'))
	print("Thread exited :", flag_index)


def handle_data(data, ser, flag_index):
	global module_ser_list, module_set_flag_list, ser_read_thread_active_flag_list, serial_ports
	for index, module in enumerate(module_list):
		if (data.find(module)>=0) and ser_read_thread_active_flag_list[flag_index] == True:
			print(ser)
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
	global serial_ports_list, ser_read_thread_list, ser_open_list, module_ser_list, ser1, ser_read_thread_active_flag_list, serial_ports
	# global base_set_flag, head_set_flag, rhand_set_flag, lhand_set_flag

	enumerate_serial_ports()
	#print("Port List :", serial_ports_list)
	for index, serial_port in enumerate(serial_ports_list):
		port_open_flag = False
		while not port_open_flag:
			try:
				print("Opening Serial_port :", serial_port)
				temp_serial = serial.Serial('/dev/'+serial_port,9600, writeTimeout = 0, timeout=1)
			except Exception as e:
				print("ERROR!!!! ",e)
				time.sleep(1)
			else:
				ser_read_thread_active_flag_list.append(True)
				temp_thread = threading.Thread(target=read_from_port, args=(temp_serial, index))
				ser_read_thread_list.append(temp_thread)
				id_enquiry(temp_serial, temp_thread)
				ser_open_list.append(temp_serial)
				print("Opened Serial_port :", serial_port)
				port_open_flag = True


	print("serial ports opened in the order are:",ser_open_list)

	print("Started Enquiry...")
	# print(ser_read_thread_list)
	while True:
		if all(item == True for item in module_set_flag_list):
			print("Found all modules...")
			break
	print("ser_read_thread_active_flag_list")
	print(ser_read_thread_active_flag_list)
	print("serial ports in the order are:",serial_ports)

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




