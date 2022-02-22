## This program would be better if random shapes were generated for each run.. but I just created
## two specific shapes to be more simple!
## I was truly stumped on figuring out the ratio part :-(

import turtle
import math
from random import randint

turtle.screensize(canvwidth=400, canvheight=400, bg="#FF91EA") ## Setting up window

text = turtle.Turtle()

def display_text():
    text.penup()
    text.color("white")
    text.speed(0)
    text.goto(-370,200)
    text.write("Area of the square (Shape 1): 22500 sq units", font=(5))
    text.goto(-370,150)
    text.write("Area of the circle (Shape 2): 11309.7336 sq units", font=(5))
    text.goto(-370,100)
    text.write("Area of the circle (Shape 2) based on ratio of points: ", font=(4))
    text.goto(-370,75)
    text.write("Not sure.. was stumped on this part :-(", font=(4))
    text.hideturtle()

display_text()

turt = turtle.Turtle()

def create_square():
    for i in range(4):
        turt.forward(250)
        turt.left(90)

def create_circle():
    turt.penup()
    turt.goto(120,70)
    turt.pendown()
    radius = 60
    turt.circle(radius)
    turt.hideturtle()

create_square()
create_circle()

area_square = 250 * 90
print("The area of the square (Shape 1) is:", area_square)

area_circle = math.pi * 60 * 60
print("The area of the circle (Shape 2) is:", area_circle)

print("The area of the circle (Shape 2) based on ratio of points is: Not sure.. was stumped on this part :-(")

point = turtle.Turtle()
square_size = 250,90 ## size of the square I created
point_size = 7
point.pencolor("red")

def move_turtle(position):
    point.up()
    point.goto(position[0], position[1])
    point.down()

def plot_random_points(origin, number_of_points, size=square_size):
    for i in range(number_of_points):
        rand_x = randint(min(origin[0], origin[0] + size[0]), max(origin[0], origin[0] + size[0]))
        rand_y = randint(min(origin[1], origin[1] + size[1]), max(origin[1], origin[1] + size[1]))
        move_turtle((rand_x, rand_y))
        point.dot(point_size) ## creates points with a size of 7

plot_random_points((0,40),25) ## origin is from 0 to 40, 25 points are plotted in the square and circle
point.hideturtle()

turtle.done()