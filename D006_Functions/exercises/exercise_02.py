def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_left():
    turn_left()
    move()


def move_right():
    turn_right()
    move()


def jump():
    move_left()
    move_right()
    move_right()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
