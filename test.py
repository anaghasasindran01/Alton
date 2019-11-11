#!/usr/bin/python3

from port_enumerate import identify_modules, serial_ports, module_list

identify_modules()

#Lose ser1, ser2, ser3 .... and use the following instead
# ser1, ser2, ser3 ... are not readable
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



# Sample usage
ser_Head.write(bytes(b'BASE FOUND!!!\r\n'))
ser_Base.write(bytes(b'HEAD FOUND!!!\r\n'))


