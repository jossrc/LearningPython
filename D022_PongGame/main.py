from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

import time

screen = Screen()
screen.title("Pong Game")
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.tracer(0)

# Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Ball
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or \
       ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle mises
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
