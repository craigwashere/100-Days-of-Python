from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(-425, 200)
        self.pendown()
        self.goto(400, 200)
        self.penup()
        self.goto(position)
        self.showturtle()
        self.y_direction = 10
        self.x_direction = 10
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        
    def move(self):
        new_x = self.xcor()+ self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)
        
    def adjust_x_speed(self, paddle_x):
        p_d_distance = (paddle_x-self.xcor())/25

        # print("ball.x_direction: {}".format(self.x_direction))
        if (paddle_x < self.xcor()):
            self.x_direction = abs(self.x_direction * p_d_distance)
        else:
            self.x_direction = (abs(p_d_distance*self.x_direction)*(-1))
            
        if (self.x_direction > 0):
            self.x_direction = max(1, min(self.x_direction, 50))
        else: #(self.x_direction < 0):
            self.x_direction = min(-1, max(self.x_direction, -50))
            
        # print("p: {0}\tb_prev:{1}\tb: {2}\td: {3}".format(
            # paddle_x, self.prev_x, self.xcor(), p_d_distance))
        # print("ball.x_direction: {}\n".format(self.x_direction))
            
    def up(self):
        new_y = self.ycor() + self.y_direction
        self.goto(self.xcor(), new_y)
    def left(self):
        new_x = self.xcor() - self.x_direction
        self.goto(new_x, self.ycor())
    def right(self):
        new_x = self.xcor() + self.x_direction
        self.goto(new_x, self.ycor())
    def down(self):
        new_y = self.ycor() - self.y_direction
        self.goto(self.xcor(), new_y)
        
    def change_y_direction(self):
        self.y_direction *= -1
        
    def change_x_direction(self):
        self.x_direction *= -1
        
    def reset(self):
        self.goto(0, 0)
        self.y_direction = 10
        self.x_direction = 10
        #self.change_x_direction()
        