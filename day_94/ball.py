from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position, direction):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        if direction > 0:
            self.color("white")
        else:
            self.color("red")
        self.goto(position)
        self.showturtle()
        self.y_direction = 10 * direction
        self.shapesize(stretch_wid=0.75, stretch_len=0.25)
        
    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)
                    
    def up(self):
        new_y = self.ycor() + self.y_direction
        self.goto(self.xcor(), new_y)
        
    def reset(self):
        self.goto(0, 0)
        self.y_direction = 10
        self.x_direction = 10
        #self.change_x_direction()
        