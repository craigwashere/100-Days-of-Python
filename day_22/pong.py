from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball((0,0))
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.tracer(0)

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.change_y_direction()

    if (ball.xcor() > 320) and (ball.distance(right_paddle) < 50):
        ball.change_x_direction()
    if (ball.xcor() < -320) and (ball.distance(left_paddle) < 50):
        ball.change_x_direction()
        
    if (ball.xcor() > 380):
        scoreboard.left_point()
        ball.reset()
        
    if (ball.xcor() < -380):
        scoreboard.right_point()
        ball.reset()
screen.exitonclick()
