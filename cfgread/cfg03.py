#!/usr/bin/env python3

# what file to open?
answ = input("what file to open?: ")

## create file object in "r"ead mode
with open(answ, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(f" the number of lines printed is {len(configlist)}")
