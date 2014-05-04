# implementation of card game - Memory

import simplegui
import random

CARD_WIDTH = 50
CARD_HEIGHT = 100

# deck of cards
deck = list(range(1, 9))
deck.extend(list(range(1, 9)))
random.shuffle(deck)

# state of cards exposed
state = []
first_click = -1
second_click = -1

# exposed cards and positions
exposed = [False] * 16
pos = []
click_pos = []

# count of turns
turns = 0

# helper function to initialize globals
def new_game():
    global deck, exposed, turns, state
    random.shuffle(deck)
    exposed = [False] * 16
    turns = 0
    state = 0
    label.set_text("Turns = " + str(turns))
    
# define event handlers
# card index returns position of card clicked
def mouseclick(pos):
    global state, first_click, second_click, click_pos, turns
    card_i = (pos[0] // 50)
    # if the card is not already exposed, exposed it and proceed 
    # with the game logic. if it is already exposed, do nothing
    if not exposed[card_i]:
        exposed[card_i] = True
        if state == 0:
            state = 1
            first_click = card_i
        elif state == 1:
            state = 2
            second_click = card_i
            turns += 1
            # label update for turns
            label.set_text("Turns = " + str(turns))
        else:
            # if first card and second card do not match,
            # flip them over
            if deck[first_click] != deck[second_click]:
                exposed[first_click] = False
                exposed[second_click] = False
                state = 1
                first_click = card_i
            # if first card and second card match, 
            # do not flip them over
            else:
                state = 1
                first_click = card_i
                
# for testing and debugging purposes; uncomment to view variables            
#    print "State:", state
#    print "First click:", first_click
#    print "Second click:",  second_click
#    print "Boolean for first click:", exposed[first_click]
#    print "Boolean for second click:", exposed[second_click]
#    print "Click Position:", pos
#    print "Card Index:", card_i
#    print "Turns: ", turns
               
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(deck)):
        if exposed[i] == True:
            canvas.draw_text(str(deck[i]), ((CARD_WIDTH * i + 13), 65), 
                             50, "White")
        else:
            canvas.draw_polygon([(i * CARD_WIDTH + 1, 0), 
                                 (i * CARD_WIDTH + 1, 100), 
                                 (i * CARD_WIDTH + CARD_WIDTH - 1 , 100), 
                                 (i * CARD_WIDTH + CARD_WIDTH - 1, 0)], 
                                1, "Green", "Green")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric