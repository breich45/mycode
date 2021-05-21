#!/usr/bin/env python3

"""
Author: Average Joe
This script does a thing
"""

def main():
    """ because i need a doc string here """
    with open("admin.rc", "a") as outFile:
        myAUTH = input("What is the OS_AUTH_URL?") # get input from user
        print("export OS_AUTH_URL=" + myAUTH, file=outFile) # put in file

        print("export OS_IDENTITY_API_VERSION=3", file=outFile) # put more stuff in the file

        myPROJ = input("What is the OS_PROJECT_NAME?") # get more stuff from user
        print("export OS_PROJECT_NAME=" + myPROJ, file=outFile) #put more stuff in file

        osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME?") # ditto
        print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile) # more ditto

        osUSER = input("What is the OS_USERNAME?") # yup, again
        print("export OS_USERNAME=" + osUSER, file=outFile) # x2

        osUSERDOM = input("What is the OS_USER_DOMAIN_NAME?") # more input. when does it end?
        print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile) # how big is this file anyways

        osPASS = input("What is the OS_PASSWORD?") # last one mebbe?
        print("export OS_PASSWORD=" + osPASS, file=outFile) # dump it with the rest

if __name__ == "__main__":
    main()

