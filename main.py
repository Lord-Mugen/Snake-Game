from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

#crear el escenario
screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate Snake")

screen.tracer(0) #desactiva la animacion por defecto

#crear - instanciar objeto serpiente
snake = Snake()

#crear instancia del objeto comida
food = Food()

scoreboard = Scoreboard()#crear objero tablero de puntos (scoreboard)
#movimientos de la serpiente
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down") #todos estos son similares a los eventListeners de js
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()


    #Condicional para detectar colision con la comida
    
    if snake.head.distance(food)<15: #Con "distance" detectamos la distancia entre la serpiente y la comida
        food.refresh() #ccambiar el lugar de la comida a medida que se come
        scoreboard.increase_score() #aumentar la puntuacion
        snake.extend()


    #Detectar los muros
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detectar si toca la cola 
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
             game_is_on = False
             scoreboard.game_over()


#final
screen.exitonclick()