"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Función para mover la manzana (food) de posición cada segundo
def moveAroud():
    #se tendrá a la manzana moviendose de uno en uno y habrá momentos en los que no se mueva
    x = randrange(-1,2) * 10
    y = randrange(-1,2) * 10
    if inside(vector(food.x + x, food.y + y)):
        food.x = food.x + x
        food.y = food.y + y

#Función que se utiliza para cambiar la dirección de la serpiente
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#Verifica si el vector posicional se encuentra en el rango del tamaño de la ventana, es decir,
#se puede utilizar para verificar si la cabeza de la serpiente chocó contra el muro.
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#Se realiza el movimiento de la serpiente, trazar a la serpiente y la manzana así como checar las condiciones de cambio:
#comer la manzana (food), chocar contra el muro etc
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    colores=["black", "green", "blue", "pink", "yellow"]
    for body in snake:
        square(body.x, body.y, 9, colores[a])

    moveAroud()
    square(food.x, food.y, 9, colores[b])
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
a=randrange(0, 5, 1)
b=randrange(0, 5, 1)
while a==b:
    a=randrange(0, 5, 1)
    b=randrange(0, 5, 1)
move()
done()
