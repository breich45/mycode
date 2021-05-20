#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

import random

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    #for catfact in r.json():
    #    print(random.choice(r))  # the .get() method returns NONE if key not found
    print(r.json())
    print(random.choice(list(r.items)))
    #for x in print(list(r)):
       #print(x.keys())
        #print(dir(x))
    #print(random.choice(r))  # the .get() method returns NONE if key not found
main()

