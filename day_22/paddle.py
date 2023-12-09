from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid=None, stretch_len=5.0)
        
    def up(self):
        if (self.ycor() < 250):
            self.forward(20)
            
    def down(self):
        if (self.ycor() > -250):
            self.backward(20)
       