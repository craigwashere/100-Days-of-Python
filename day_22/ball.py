from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(position)
        self.color("white")
        self.y_direction = 10
        self.x_direction = 10
        
    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)
    
    
    def change_y_direction(self):
        self.y_direction *= -1
        
    def change_x_direction(self):
        self.x_direction *= -1
        
    def reset(self):
        self.goto(0, 0)
        self.change_x_direction()