#
# Game Description from: 
# TBD

from turtle import Turtle, Screen
from ship import Ship
from ball import Ball
from grid import Grid
from scoreboard import Scoreboard
import time
import random
import threading

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 825, height = 600)
screen.title("Space Invaders")
screen.listen()

# add new shapes
screen.register_shape('./img/ship.gif')
screen.register_shape('./img/invader_lvl_1-2.gif')
screen.register_shape('./img/invader_lvl_3-4.gif')
screen.register_shape('./img/invader_lvl_5.gif')
screen.register_shape('./img/boom.gif')
screen.register_shape('./img/boom2.gif')

ship = Ship((-250, -250))

BOMB_TIMER = 30
HARD_MODE = False

balls = []
balls2 = []
exploding_invaders = []

grid = Grid()
scoreboard = Scoreboard()

screen.onkeypress(ship.right, "Right")
screen.onkeypress(ship.left, "Left")

def fire2():
    invader = random.choice(grid.grid)
    balls2.append(Ball((invader.xcor(), invader.ycor()), -1))

def fire():
    global balls
    balls.append(Ball((ship.xcor(), ship.ycor()), 1))
screen.onkeypress(fire, "space")

game_is_on = True

def quit():
    global game_is_on
    print("quit")
    game_is_on = False
screen.onkeypress(quit, "q")

screen.tracer(0)
wait_time = 0.05
ball2_timer = random.randint(0, BOMB_TIMER)

def reset():
    wait_time = 0.05
    
def remove_exploding_invader(invader: Turtle):
    invader.hideturtle()
    exploding_invaders.remove(invader)
    invader = None
    
def remove_exploding_ship(ship: Turtle):
    ship.shape('./img/ship.gif')
    
def check_for_collision(ball: Ball) -> bool:
    for j, invader in enumerate(grid.grid):
        if ball.distance(invader) < 25:
            scoreboard.update_score(invader.shape())
            invader.shape('./img/boom.gif')
            exploding_invaders.append(invader)
            grid.grid.pop(j)
            
            threading.Timer(0.1, remove_exploding_invader, args=[invader]).start()
            
            ball.hideturtle()
            ball = None
            return True
            
    return False

while game_is_on:
    time.sleep(wait_time)
    
    for j, ball in enumerate(balls):
        ball.move()
        if check_for_collision(ball) == False:
            if ball.ycor() > 300:
                balls.pop(j)
                ball = None
        else:
            balls.pop(j)
            invader_count = len(grid.grid)
            if invader_count < 14:
                wait_time *= 0.75
                BOMB_TIMER -= 1
            elif invader_count < 7:
                BOMB_TIMER -= 2
                wait_time *= 0.5
            elif invader_count == 0:
                game_is_on = False

    for j, ball2 in enumerate(balls2):
        ball2.move()
        if ship.shape() == './img/ship.gif':
            if ball2.distance(ship) < 50:
                ship.shape('./img/boom2.gif')
                threading.Timer(0.3, remove_exploding_ship, args=[ship]).start()
                balls2.pop(j)
                ball2.hideturtle()
                ball2 = None

                scoreboard.balls_left -= 1
                scoreboard.update_scoreboard()
                if scoreboard.balls_left <= 0:
                    game_is_on = False
                    break;

    for invader in grid.grid:
        if (invader.distance(ship) < 40) or (invader.ycor() < -275): 
            game_is_on = False
            break
            
    if ball2_timer == 0:
        fire2()
        ball2_timer = random.randint(0, BOMB_TIMER)
    else:
        ball2_timer -= 1
        
    grid.move()
       
    screen.update()
        
screen.exitonclick()