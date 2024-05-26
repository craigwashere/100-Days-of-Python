from turtle import Turtle, Screen, TK
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

valid_bet = False
while valid_bet == False:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet not in colors:
        TK.messagebox.showerror(title="Error:", message="Turtle not found!")
    else:
        valid_bet = True

is_race_on = True
winner = ""
while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            
# print(f"Winner: {winner}")            
if winner[0] == user_bet:
    TK.messagebox.showinfo(title="Turtle Race:", message=f"You bet on {user_bet}.\nYou Win!")
else:
    TK.messagebox.showinfo(title="Turtle Race:", message=f"You bet on {user_bet}, {winner} won.\nYou Lose")
    
screen.exitonclick()