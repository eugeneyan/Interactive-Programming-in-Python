# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
cash = 30
game_deck = []
player_hand = []
dealer_hand = []
player_bust_outcome = ("Crap...", "Damn...", "Curses...", "No Way...", "I'm outta here...")
player_win_outcome = ("Oh yeah!", "Show me the money!", "Take that sucka!", "Who's your daddy?!", "Booyah!")
player_lose_outcome = ("He's gotta be cheating...", "Where's my rabbit's foot?", "The house always wins...")
dealer_outcome1 = ""
dealer_outcome2 = ""
overall_outcome = ""
buys = 0
start_text = "First $30 on the House! Click Buy In when you're broke."
win_streak = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
   
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        card_str = ""
        for card in self.cards:
            card_str += str(card) + " "
        return "Hand contains: " + card_str

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        # let hand_value be the sum of card values 
        # if the hand has no Aces:
        #     return hand_value
        # else:
        #	  if hand_value + 10 <= 21:
        #         return hand_value + 10
        #     else:
        #         return hand_value
        self.ace_present = False
        self.hand_value = 0
        for card in self.cards:
            card_value = VALUES[card.get_rank()]
            self.hand_value += card_value
            if card_value == 1:
                self.ace_present = True
            
        if not self.ace_present:
            return self.hand_value
        else:
            if self.hand_value + 10 <= 21:
                return self.hand_value + 10
            else:
                return self.hand_value
   
    def draw(self, canvas, pos):
    # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            card.draw(canvas, pos)
            pos = (pos[0] + CARD_SIZE[0]/2, pos[1])
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
                
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        s = ""
        for i in range(len(self.deck)):
            s += str(self.deck[i]) + " "
        return "Deck contains " + s

#define event handlers for buttons
def deal():
    global in_play, cash, dealer_hand, player_hand, game_deck, player_outcome, dealer_outcome1, dealer_outcome2, overall_outcome
    if cash < 10:
        overall_outcome = "YOU'RE BROKE!"
        return 
    else:
        if in_play:
            cash -= 10
            player_outcome = "What did I do that for?!"
            dealer_outcome1 = "That will be $10."
            dealer_outcome2 = "Hit or Stand?"
            overall_outcome = ""
        else:
            player_outcome = "Hmmm..."
            dealer_outcome1 = "Hit or Stand?"
            dealer_outcome2 = ""
            overall_outcome = ""

    game_deck = Deck()
    game_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())

    # for debugging purposes
    # print "Player " + str(player_hand) + "| Dealer " + str(dealer_hand)
    # print game_deck
    # your code goes here
    
    in_play = True

def hit():
    global in_play, game_deck, player_hand, cash, player_outcome, dealer_outcome1, dealer_outcome2, overall_outcome, win_streak
    # if the hand is in play, hit the player
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(game_deck.deal_card())
        overall_outcome = ""
        # for debugging purposes
        # print "Player " + str(player_hand)
        # if busted, assign a message to outcome, update in_play and 
        
        if player_hand.get_value() > 21:
            in_play = False
            cash -= 10
            player_outcome = random.choice(player_bust_outcome)
            dealer_outcome1 = "That's bad luck."  
            dealer_outcome2 = "Deal again?"
            overall_outcome = "DEALER WINS!"
            win_streak = 0
            # for debugging purposes
            # print "Cash: $" + str(cash)
    
def stand():
    global in_play, game_deck, dealer_hand, cash, player_outcome, dealer_outcome1, dealer_outcome2, overall_outcome, win_streak
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(game_deck.deal_card())
    # assign a message to outcome, update in_play and 
    
        if dealer_hand.get_value() > 21:
            player_outcome = "Whew he busted!"
            dealer_outcome1 = "Lucky you."
            dealer_outcome2 = "Deal again?"
            overall_outcome = "PLAYER WINS!"
            cash += 10
            win_streak += 1
            if win_streak == 3:
                player_outcome = "I'm on a roll!"
            if win_streak == 7:
                player_outcome = "Greed is Good"
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                player_outcome = random.choice(player_lose_outcome)
                dealer_outcome1 = "Lucky me."
                dealer_outcome2 = "Deal again?"
                overall_outcome = "DEALER WINS!"
                cash -= 10
                win_streak = 0
            else:
                player_outcome = random.choice(player_win_outcome)
                dealer_outcome1 = "Nice one."
                dealer_outcome2 = "Deal again?"
                overall_outcome = "PLAYER WINS!"
                cash += 10
                win_streak += 1
                if win_streak == 3:
                    player_outcome = "I'm on a roll!"
                elif win_streak == 7:
                    player_outcome = "Greed is Good"
        # for debugging purposes
        # print "Dealer " + str(dealer_hand)
        # print str(player_hand.get_value()) 
        # print str(dealer_hand.get_value())
        # print "Cash: $" + str(cash)
    in_play = False

def buy_in():
    global cash, overall_outcome, buys
    cash += 100
    buys += 1
    overall_outcome = "There goes $" + str(buys) + "00..."
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below    
    card = Card("S", "A")
    player_hand.draw(canvas, [50, 470])
    dealer_hand.draw(canvas, [50, 30])
    if in_play:
        canvas.draw_image(card_back, (CARD_BACK_CENTER[0]/2, CARD_BACK_CENTER[1]), (CARD_BACK_SIZE[0]/2, CARD_BACK_SIZE[1]), (69, 80), (CARD_SIZE[0]/2, CARD_SIZE[1]))
    canvas.draw_text("BLACK", (30, 330), 90, "Black")
    canvas.draw_text("JACK", (340, 330), 90, "White")
    canvas.draw_text(start_text, (70, 360), 20, "Black")
    canvas.draw_text("Dealer", (300, 70), 50, "Black")
    canvas.draw_text("Player", (300, 505), 50, "White")
    canvas.draw_text(player_outcome, (300, 538), 25, "White", "sans-serif")
    canvas.draw_text(dealer_outcome1, (300, 95), 25, "Black", "sans-serif")
    canvas.draw_text(dealer_outcome2, (300, 120), 25, "Black", "sans-serif")
    canvas.draw_text(overall_outcome, (160, 410), 40, "White")
    canvas.draw_text("Cash: $" + str(cash), (480, 485), 20, "White")
    canvas.draw_text("Streak: " + str(win_streak), (480, 505), 20, "White")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Buy In", buy_in, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
# for debugging purposes
# print player_hand.get_value()

# remember to review the gradic rubric