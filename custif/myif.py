#!/usr/bin/env python3

""" assign a letter grade to a test score """

score = int(input("What is the score?: ")) #get user input

if score in range(90, 101):  # evaluate the score 
    print("You got an A!!")
elif score in range(80, 90):  # evaluate the score 
    print("You got an B!")
elif score in range(70, 80):  # evaluate the score 
    print("You got an C")
elif score in range(60, 70):  # evaluate the score 
    print("You got a D")
elif score <= 59:  # evaluate the score 
    print("You got a F :(")
else:
    print("Not a valid score!") # if score is not 1-100 throw error
