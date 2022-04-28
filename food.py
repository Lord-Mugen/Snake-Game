from this import d
from turtle import Turtle

#generar numero aleatorio
import random

color = ["Blue", "Green"]
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(strech_len=0.5, strech_wid=0.5)
        self.color("green")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)