# Day 6 is based on the Reeborg game
# This is the solution for the Maze challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()

turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
