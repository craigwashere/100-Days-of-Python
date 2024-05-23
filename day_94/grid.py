from turtle import Turtle

ship_skins = ['./img/invader_lvl_1-2.gif', './img/invader_lvl_1-2.gif', './img/invader_lvl_3-4.gif', './img/invader_lvl_3-4.gif', './img/invader_lvl_5.gif']

class Grid:
    def __init__(self):
        self.grid = []
        self.x_direction = 1
        
        for i, skin in enumerate(ship_skins):
            for j in range(7):
                block = Turtle(skin)
                block.penup()
                block.shapesize(stretch_wid=2.5, stretch_len=2.5)
                block.goto(-380+(j*40), 75+(i*30))
                self.grid.append(block)

    def move(self):
        self.check_boundry()
        for j, block in enumerate(self.grid):
            current_x = block.xcor()
            new_x = current_x + (10*self.x_direction)
            block.goto(new_x, block.ycor())
            
    def move_down(self):
        for block in self.grid:
            block.goto(block.xcor(), block.ycor()-15)
            
    def check_boundry(self):
        for block in self.grid:
            if (block.xcor() > 380) or (block.xcor() < -380):
                self.x_direction *= -1
                self.move_down()
                return