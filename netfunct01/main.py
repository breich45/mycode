#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons

#function to reboot ip's
def rebootpush(work2do): #ips is a list of ip's
    for sw in work2do:
        print(f'{str(crayons.green("Handshaking"))}. .. ... connecting with {sw}')
        print(f'REBOOTING NOW!!')
	


# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print(f'{str(crayons.green("Handshaking"))}. .. ... connecting with {coffeetime}')
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    #print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    #commandpush(work2do) # call function to push commands to devices

    # push reboot command to list of switch IP from file
    myfile01 = input("enter filename containing switch IPs: ")
    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file
    with open("myfile01.txt", "r") as myfile01:
    	rebootpush(myfile01) # call function to push reboot commands to devices

# call our main function
main()

