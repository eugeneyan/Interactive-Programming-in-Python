# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = []
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
player1_score = 0
player2_score = 0

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]
    elif direction == LEFT:
        ball_vel = [-random.randrange(120, 240) / 60, -random.randrange(60, 180) / 60]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global player1_score, player2_score # these are ints
    spawn_ball(RIGHT)
    player1_score = 0
    player2_score = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel, player1_score, player2_score
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    # collision with horizontal walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif HEIGHT - ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # left gutter test
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= 1.1
            ball_vel[0] = -ball_vel[0]
        else:
            player2_score += 1
            spawn_ball(RIGHT)
            
    # right gutter test
    if ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
        if paddle2_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= 1.1
            ball_vel[0] = -ball_vel[0]
        else:
            player1_score += 1
            spawn_ball(LEFT)
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "white", "white") 
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= 0 + HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel >= 0 + HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - 1 - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([(0, paddle1_pos - HALF_PAD_HEIGHT), (0, paddle1_pos + HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT)], 1, "white", "white")  
    canvas.draw_polygon([(WIDTH - 1, paddle2_pos - HALF_PAD_HEIGHT), ((WIDTH - 1), paddle2_pos + HALF_PAD_HEIGHT), ((WIDTH - 1 - PAD_WIDTH), paddle2_pos + HALF_PAD_HEIGHT), ((WIDTH - 1 - PAD_WIDTH), paddle2_pos - HALF_PAD_HEIGHT)], 1, "white", "white")
    
    # draw scores
    canvas.draw_text(str(player1_score), (150, 100), 20, "white")
    canvas.draw_text(str(player2_score), (450, 100), 20, "white")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc

    if key == simplegui.KEY_MAP["q"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["o"]:
        paddle1_vel -= acc    
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

    if key == simplegui.KEY_MAP["q"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["o"]:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)

# start frame
new_game()
frame.start()
