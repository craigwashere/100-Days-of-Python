from turtle import Turtle
import atexit

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        
        try:
            with open("hiscore.txt") as high_score_file:
                self.high_score = int(high_score_file.read())
        except FileNotFoundError:
            self.high_score = 0
            
        self.update_score()
        atexit.register(self.cleanup)
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg = f"Score: {self.score}  High Score: {self.high_score}", 
            move = False, align = 'Center', font = ('Arial', 18, 'normal'))
            
    def reset(self):
        self.high_score = self.score if self.score > self.high_score else self.high_score
        self.score = 0
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(arg = f"GAME OVER", move = False, 
            align = 'Center', font = ('Arial', 18, 'normal'))
            
    def cleanup(self):
        with open("hiscore.txt","w") as high_score_file:
            high_score_file.write(str(self.high_score))
        