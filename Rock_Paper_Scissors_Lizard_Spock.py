# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "Invalid move"
    return number

#test name_to_number()
#print name_to_number("Spock")
#print name_to_number("rock")
#print name_to_number("paper")
#print name_to_number("lizard")
#print name_to_number("scissors")

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "Invalid number"
    return name

#test number_to_name
#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)

import random

def rpsls(player_choice): 
    print
    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice
    calc = (player_number - comp_number) % 5
    '''
    #print test for calc
    '''
    print "calc:", calc
    if calc == 1 or calc == 2:
        print "Player wins!"
    elif calc == 3 or calc == 4:
        print "Computer wins!"
    elif calc == 0:
        print "Player and computer tie!"
    else:
        print "Calc_error"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

