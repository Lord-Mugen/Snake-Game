from turtle import Turtle
import random #generar numero aleatorio

color = ["Blue", "Green"]
class Food(Turtle): #creamos la clase y por medio de los parentesis de les damos la herencia sus hijos.

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.refresh() #hacemos que el lugar de spawn de la comida sea aleatorio cada que se abra el screen

    def refresh(self): #metodo para que el lugar de la comida sea aleatoria
        random_x = random.randint(-200, 200) # si esta medida o la de abajo pasan de 300 se saldrán de la pantalla
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)