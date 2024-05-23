from turtle import Turtle

class Ship(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('./img/ship.gif')
        self.setx(position[0])
        self.sety(position[1])
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2.0)
        self.length = 40
        
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
            