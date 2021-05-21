#!/usr/bin/env python3

""" Created: Average Joe
    Simple dice game """

#import stuff
#from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

def main():
    """ execute teh main logic """
    cheater1 = Cheat_Swapper()  #create player object1
    cheater2 = Cheat_Loaded_Dice() #create player object2

    cheater1.roll()  #roll the dice!
    cheater2.roll()  #roll the dice

    cheater1.cheat() # apply the cheat
    cheater2.cheat() #apply the cheat

    print("Cheater 1 rolled" + str(cheater1.get_dice())) # get the values of the dice rolls
    print("Cheater 2 rolled" + str(cheater2.get_dice())) # get teh value of the dice rolls

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):  #  determine if it was a tie.
        print("Draw!") 					      # print the result

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()): #  determine the winner
        print("Cheater 1 wins!") # print result

    else:
        print("Cheater 2 wins!") # print the result

if __name__ == '__main__':
    main()
