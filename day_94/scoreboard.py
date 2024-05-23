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
        
    def update_score(self, shape: str):
        if shape == './img/invader_lvl_1-2.gif':
            self.block_score += 10
        elif shape == './img/invader_lvl_3-4.gif':
            self.block_score += 20
        else:
            self.block_score += 30
        self.update_scoreboard()
            
    def update_scoreboard(self):
        scoreboard_font = ("Courier", 20, "normal")
        text_y = 270
        self.clear()
        self.goto(-200, text_y)
        self.write(f'{self.block_score:04}', align = "center", 
            font = scoreboard_font)
        self.goto(300, text_y)
        self.write(f'{self.balls_left:02}', align = "center", 
            font = scoreboard_font)
                