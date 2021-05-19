#!/usr/bin/env python3

import netifaces

#print(netifaces.interfaces())

for i in netifaces.interfaces():
    #print(netifaces.ifaddresses(i))
    print(f'\n******** Details of Interface - {i} ************')
    try:
    	print(f"{i} MAC: {netifaces.ifaddresses(i)[netifaces.AF_LINK]}")
    	print(f"{i} IP: {netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']}")
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message


