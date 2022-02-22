## This program creates a random triangle and bisects its 3 angles by meeting in the middle for each line.
## Each angle and bisection is shown with different colors and shapes: red circle, green square, and blue turtle!

from turtle import Turtle, Screen
from random import seed, randint ## seed is random number generator initialization

WIDTH, HEIGHT = 425, 425 ## size of Turtle Graphics screen

def bisect(turtle1, turtle2):

    position_2 = turtle2.position()

    while True:
        turtle1.setheading(turtle1.towards(turtle2))
        turtle1.forward(1)
        position_1 = turtle1.position()
        if int(position_1[0]) == int(position_2[0]) and int(position_1[1]) == int(position_2[1]):
            break

        turtle2.setheading(turtle2.towards(turtle1))
        turtle2.forward(1)
        position_2 = turtle2.position()
        if int(position_2[0]) == int(position_1[0]) and int(position_2[1]) == int(position_1[1]):
            break

seed() ##pseudo-random
screen = Screen()
vertices = []

for i in range(3):
    x = randint(-WIDTH//2, WIDTH//2)
    y = randint(-HEIGHT//2, HEIGHT//2)
    vertices.append((x, y))

A, B, C = vertices

turtle_AtoB = Turtle(shape = 'circle')
turtle_AtoB.pencolor("red")
turtle_AtoB.penup()
turtle_AtoB.goto(A)
turtle_AtoB.pendown()

turtle_BtoA = Turtle(shape = 'circle')
turtle_BtoA.pencolor("red")
turtle_BtoA.penup()
turtle_BtoA.goto(B)
turtle_BtoA.pendown()

bisect(turtle_AtoB, turtle_BtoA) ## bisect function is used

turtle_BtoA.hideturtle()
turtle_AtoB.setheading(turtle_AtoB.towards(C))
turtle_AtoB.goto(C)
turtle_AtoB.hideturtle()


turtle_BtoC = Turtle(shape = 'square')
turtle_BtoC.pencolor("green")
turtle_BtoC.penup()
turtle_BtoC.goto(B)
turtle_BtoC.pendown()

turtle_CtoB = Turtle(shape = 'square')
turtle_CtoB.pencolor("green")
turtle_CtoB.penup()
turtle_CtoB.goto(C)
turtle_CtoB.pendown()

bisect(turtle_BtoC, turtle_CtoB)

turtle_CtoB.hideturtle()
turtle_BtoC.setheading(turtle_BtoC.towards(A))
turtle_BtoC.goto(A)
turtle_BtoC.hideturtle()


turtle_CtoA = Turtle(shape = 'turtle')
turtle_CtoA.pencolor("blue")
turtle_CtoA.penup()
turtle_CtoA.goto(C)
turtle_CtoA.pendown()

turtle_AtoC = Turtle(shape = 'turtle')
turtle_AtoC.pencolor("blue")
turtle_AtoC.penup()
turtle_AtoC.goto(A)
turtle_AtoC.pendown()

bisect(turtle_CtoA, turtle_AtoC)

turtle_AtoC.hideturtle()
turtle_CtoA.setheading(turtle_CtoA.towards(B))
turtle_CtoA.goto(B)
turtle_CtoA.hideturtle()

screen.exitonclick()