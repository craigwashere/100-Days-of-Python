from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=5.0)
        self.length = 55
        
    def right(self):
        if (self.xcor() < 350):
            self.forward(20)
            
    def left(self):
        if (self.xcor() > -360):
            self.backward(20)
    
    def shorten(self):
        if (self.length == 55):
            self.length = 35
            self.shapesize(stretch_wid=0.5, stretch_len=3.0)
        
    def reset(self):
        self.shapesize(stretch_wid=0.5, stretch_len=5.0)
        self.length = 55
    