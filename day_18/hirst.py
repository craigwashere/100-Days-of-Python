#import colorgram

# colors = colorgram.extract('index.jpg', 30)

# for color in colors:
    # red   = color.rgb.r
    # green = color.rgb.g
    # blue  = color.rgb.b
    # rgb_colors.append((red, green, blue))

import turtle
import random
def draw_row(canv_width):
    for _ in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(canv_width/10)

rgb_colors = [ (244, 235, 46), (196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), 
    (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22), (202, 34, 91), (186, 16, 9),
    (19, 18, 42),(216, 141, 191), (57, 15, 10), (88, 8, 28), (227, 161, 9), (78, 212, 157), (67, 73, 221),
    (13, 95, 61), (78, 194, 225), (239, 158, 215), (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238)]
    
canv_width, canv_height = turtle.screensize()
turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")

# height = 300
# width = 400
tim.penup()
x = -canv_width*.5
y = -canv_height*.5
for _ in range(10):
    tim.goto(x, y)
    draw_row(canv_width)
    y = y + canv_height/10
    
    

turtle.exitonclick()
    