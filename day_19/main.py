# 178
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forwards():
    # tim.forward(10)

# def  move_backwards():
    # tim.backward(10)
    
# def turn_left():
    # tim.left(5)
    
# def turn_right():
    # tim.right(5)
  
# def reset():
    # tim.reset()
    

# screen.listen()
# screen.onkeypress(key="w", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=turn_left)
# screen.onkeypress(key="d", fun=turn_right)
# screen.onkey(key="c", fun=reset)
# screen.exitonclick()

# 179 - 181
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
new_y = -100
for color in colors:
    temp_turtle = Turtle(shape="turtle")
    temp_turtle.color(color)
    temp_turtle.penup()
    turtles.append(temp_turtle)

    temp_turtle.goto(x=-230, y=new_y)
    new_y = new_y + 50

user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")

is_race_on = True
winner = ""
while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            
print(f"Winner: {winner}")            
if winner[0] == user_bet:
    print("Winner")
else:
    print("Loser")
    
screen.exitonclick()