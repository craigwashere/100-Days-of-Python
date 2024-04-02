from turtle import Turtle
import random

COLORS = ['red', 'orange', 'brown', 'yellow', 'green', 'blue']

class Grid:
    def __init__(self):
        self.grid = []
        for i in range(len(COLORS)):
            for j in range(20):
                block = Turtle("square")
                block.penup()
                block.shapesize(stretch_wid=1, stretch_len=2)
                block.goto(-395+(j*41), 150-(i*21))
                block.color(COLORS[i])
                self.grid.append(block)
