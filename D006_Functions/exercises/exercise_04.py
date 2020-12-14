def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_right():
    turn_right()
    move()


def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    move_right()
    move_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
