import turtle
import turtle as t
from turtle import Screen
import random
import colorgram

tim = turtle.Turtle()
tim.speed("fastest")
turtle.colormode(255)

colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tim.hideturtle()
tim.penup()
tim. goto(-200, -200)



def dot_row():
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)
        tim.penup()

def move_next_row():
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(500)
    tim.right(90)
    tim.forward(20)
    tim.right(90)

for i in range(10):
    dot_row()
    move_next_row()



screen = Screen()
screen.exitonclick()
screen.setup(width=400, height=300)