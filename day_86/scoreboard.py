from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.block_score = 0
        self.balls_left = 3
        self.player = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.block_score, align = "center", 
            font = ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.balls_left, align = "center", 
            font = ("Courier", 80, "normal"))
        self.goto(300, 200)
        self.write(self.player, align = "center", 
            font = ("Courier", 80, "normal"))
        
    def block_point(self, ycor):
        if (ycor > 125):
            self.block_score += 7
        elif (ycor > 85):
            self.block_score += 4
        else:
            self.block_score += 1
        self.update_scoreboard()
        