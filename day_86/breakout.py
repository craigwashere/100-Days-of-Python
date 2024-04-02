#
# Game Description from: 
# https://www.reddit.com/r/retrogaming/comments/7m6oij/lets_compare_breakout_vs_arkanoid_vs_kirbys_block/
#
# You're dealing with a brick wall of eight rows, and you're bouncing a ball 
# against it with a paddle. Each row of the wall is a specific colour. Points
# are 1 point for yellow, 3 for the green, 7 for red. To make the game more 
# challenging, the speed of the game increases after 4 hits and again at 12 
# hits and to the highest speeds in orange and red rows. The paddle decreases 
# by half the size when the red row is broken through. If the player loses the 
# ball three times, it's game over.
#

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from grid import Grid
from scoreboard import Scoreboard
import time

paddle = Paddle((-250, -250))

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 825, height = 600)
screen.title("Breakout")
screen.listen()
ball = Ball((0,0))
screen.onkeypress(paddle.right, "Right")
screen.onkeypress(paddle.left, "Left")
# screen.onkeypress(ball.up, "Up")
# screen.onkeypress(ball.down, "Down")

scoreboard = Scoreboard()
grid = Grid()

screen.tracer(0)
num_of_hits = 0
wait_time = 0.05

def reset():
    wait_time = 0.05
    num_of_hits = 0
    ball.reset()
    paddle.reset()

game_is_on = True
while game_is_on:
    time.sleep(wait_time)
    screen.update()
    b_xcor = ball.xcor()
    b_ycor = ball.ycor()
    ball.move()
    
    for t in grid.grid:
        if ball.distance(t) < 25:
            t_ycor = t.ycor()
            t_xcor = t.xcor()
            if ( (b_ycor > t_ycor-12) and (b_ycor < t_xcor+12) ):
                ball.change_x_direction()
            else:
                ball.change_y_direction()
            grid.grid.remove(t)
            scoreboard.block_point(t_ycor)
            t.hideturtle()
            if len(grid.grid) == 0:
                game_is_on = False
            
            if num_of_hits < 13:
                num_of_hits += 1
                if num_of_hits == 4 or num_of_hits == 12:
                    wait_time *= .75
                    
            break;
    
    if (b_ycor > 180) and (ball.y_direction > 0):
        ball.change_y_direction()
        paddle.shorten()

    if (b_ycor < -240) and (b_ycor > -260):
        p_xcor = paddle.xcor()
        if (b_xcor > p_xcor-paddle.length) and (b_xcor < p_xcor+paddle.length) and (ball.y_direction < 0):
            ball.adjust_x_speed(paddle.xcor())
            ball.change_y_direction()
            
    if (ball.ycor() < -280):
        scoreboard.balls_left -= 1
        scoreboard.update_scoreboard()
        if scoreboard.balls_left == 0:
            game_is_on = False
        reset()
        
    if (ball.xcor() > 395):
        ball.change_x_direction()
        
    if (ball.xcor() < -395):
        ball.change_x_direction()
        
screen.exitonclick()