## Derrick is determined to encounter a lion and become a Moran... TODAY!!

import turtle

t = turtle.Turtle()
turtle.screensize(canvwidth=600, canvheight=600, bg="#728C00")
t.speed = 0
t.pensize(8)
t.penup()
t.goto(0,-100)
t.pendown()

## Lion's head
t.fillcolor("#DAA520")
t.begin_fill()
for i in range(36):
    t.forward(30)
    t.left(10)
t.end_fill()

## Lion's eyes
t.penup()
t.goto(-80,90)
t.pendown()

t.left(90)
for i in range(45):
    t.forward(2)
    t.right(4)

t.penup()
t.goto(50,90)
t.pendown()

t.left(-180)
for i in range(45):
    t.forward(2)
    t.right(4)

## Lion's nose
t.penup()
t.goto(0,50)
t.pendown()

t.setheading(0)

for i in range(5):
    t.forward(25)
    t.right(120)
starting_nose_x = t.xcor()
starting_nose_y = t.ycor()

## Lion's mouth
t.left(120)
t.forward(10)
for i in range(4):
    t.right(16)
    t.forward(17)

t.penup()
t.goto(starting_nose_x,starting_nose_y)
t.pendown()
t.setheading(-60)

t.forward(10)
for i in range(4):
    t.left(16)
    t.forward(17)

t.penup()
t.goto(-19,-.10)
t.pendown()
t.right(100)
for i in range(10):
    t.forward(12)
    t.left(21)

## Lion's ears
t.fillcolor("#B8860B")
t.begin_fill()
t.penup()
t.goto(150,250)
t.pendown()
for i in range(36):
    t.forward(5)
    t.left(10)
t.pendown()
t.end_fill()

t.fillcolor("#B8860B")
t.begin_fill()
t.penup()
t.goto(-80, 240)
t.pendown()
for i in range(36):
    t.forward(5)
    t.left(10)
t.pendown()
t.end_fill()

t.ht() ## hide turtle

## Derrick
derrick = turtle.Turtle()      #instantiate a new turtle object called 'a'
derrick.shape("circle")
derrick.fillcolor("#966F33")
derrick.width(8)
derrick.speed(1)

derrick.ht()           #make the turtle invisible
derrick.pencolor("#654321")
derrick.penup()                #don't draw when turtle moves
derrick.goto(-400, -400)       #move the turtle to a location
derrick.showturtle()           #make the turtle visible
derrick.pendown()              #draw when the turtle moves
derrick.goto(-75, -75)           #move the turtle to a new location

style = ("Arial", 40, "bold")
turtle.color("#FF0000")
turtle.write("You have reached the lion, Derrick! You are now a MORAN!", font=style, align="center")
turtle.ht()

turtle.done() ## screen stays until exit yourself