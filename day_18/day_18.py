import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")

def random_color():
    red   = random.randint(0, 255)
    green = random.randint(0, 255)
    blue  = random.randint(0, 255)
    return (red, green, blue)

# 171    
# directions = [0, 90, 180, 270]
# tim.pensize(15)

# for _ in range(200):
    # tim.color(random_color())
    # tim.forward(30)
    # tim.setheading(random.choice(directions))

# 172    
for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)
