# template for "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
width = 200
height = 200
stopped = 0
success = 0
first_stop_click = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    minutes = int(time // 600)
    seconds = int((time - minutes * 600) // 10)
    tenths = int(time - minutes * 600 - seconds * 10)
    if seconds >= 10:
        return str(minutes) + ":" + str(seconds) + "." + str(tenths)
    else:
        return str(minutes) + ":" + "0" + str(seconds) + "." + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global first_stop_click
    timer.start()
    first_stop_click = True
    
def stop():
    global stopped, success, first_stop_click 
    timer.stop()
    if first_stop_click:
        first_stop_click = False
        stopped += 1
        if time % 10 == 0:
            success += 1
    
def reset():
    global time, stopped, success
    timer.stop()
    time = 0
    stopped = 0
    success = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1
    
# define draw handler
def draw(canvas):
    """draw timer"""
    canvas.draw_text(format(time), (50, 110), 40, "White")
    """draw score counter"""
    canvas.draw_text(str(success) + "/" + str(stopped), (165, 18), 20, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# register event handlers
start_button = frame.add_button("Start", start, 100)
stop_button = frame.add_button("Stop", stop, 100)
reset_button = frame.add_button("Reset", reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
