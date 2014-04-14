# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
secret_number = 0
upper_bound = 101
player_guess = 0
remaining_guesses = 7
guesses_allowed = 7
result = 0

# helper function to start and restart the game
def new_game():
    global secret_number, remaining_guesses
    secret_number = random.randrange(0, upper_bound)
    remaining_guesses = guesses_allowed
    """to view secret_number at each new game"""
    print
    print "==================="
    print "Secret number is", secret_number
    print "==================="
    print
    print "New game. Range is from 0 to", (upper_bound - 1)
    print "Number of remaining guesses is", (remaining_guesses)
    
# define event handlers for control panel
def range100():
    global upper_bound, remaining_guesses, guesses_allowed
    upper_bound = 101
    guesses_allowed = 7
    remaining_guesses = guesses_allowed
    new_game()
    
def range1000():
    global upper_bound, remaining_guesses, guesses_allowed
    upper_bound = 1001
    guesses_allowed = 10
    remaining_guesses = guesses_allowed
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global player_guess, remaining_guesses
    player_guess = int(guess)
    """print empty line"""
    print
    """print player guess"""
    print "Guess was", player_guess
    """print number of remaining guesses"""
    remaining_guesses -= 1
    #condition: remaining guesses >= 0 and correct guess#
    if remaining_guesses >= 0 and player_guess == secret_number:
        print "Number of remaining guesses is", remaining_guesses
        print "Correct! Let's go again!"
        print
        new_game()
    #condition: remaining guesses == 0 and wrong guess
    elif remaining_guesses == 0 and player_guess != secret_number:
        print "Number of remaining guesses is", remaining_guesses
        print "Game Over! Would you like to try again?"
        print
        new_game()
    #condition: remaining guesses >= 0 and guess too low
    elif remaining_guesses >= 0 and player_guess < secret_number:
        print "Number of remaining guesses is", remaining_guesses
        print "Higher!"
    #condition: remaining guesses >= 0 and guess too high
    elif remaining_guesses >= 0 and player_guess > secret_number: 
        print "Number of remaining guesses is", remaining_guesses
        print "Lower!"
    
# create frame

frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements

inp = frame.add_input("Enter a Guess", input_guess, 100)
frame.add_button("Range: 0 - 100", range100, 120)
frame.add_button("Range: 0 - 1000", range1000, 120)

# call new_game and start frame

new_game()
frame.start()

# always remember to check your completed program against the grading rubric
