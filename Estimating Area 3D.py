## Quite difficult project for me.. could not figure out how to incorporate the random points in a 3D version :-(
## I did more hard coding with the shape sizes, which is bad, I know.. :-( but I got the random shapes in this time!
## ALSO check compiler for the surface area / volume print outs

from vpython import *
from fractions import Fraction
import random as rand
import math

outer = rand.randint(1, 2)
if outer == 1:
    box(pos=vector(0, 0, 0), size=vector(5, 5, 5), color=color.magenta, opacity=0.5) ## Cube
    surface_area = 6 * 25 ## Must take into account for BOTH surface area and volume because we are working with 3D shapes
    volume = 5 * 5 * 5
    print("The surface area of the outer shape is:", surface_area)
    print("The volume of the outer shape is:", volume)

else:
    box(pos=vector(0, 0, 0), size=vector(4, 4, 5), color=color.orange, opacity=0.5)  ## Rectangular prism
    surface_area = (2*16) + (2*20) + (2*20)
    volume = 4 * 4 * 5
    print("The surface area of the outer shape is:", surface_area)
    print("The volume of the outer shape is:", volume)

inner = rand.randint(1, 2)
if inner == 1:
    sphere(pos=vector(0, 0, 0), radius=1, color=color.purple, opacity=0.3) ## Sphere
    surface_area = 4 * math.pi * 1
    volume = Fraction('4/3') * math.pi * 1
    print("The surface area of the inner shape is:", surface_area)
    print("The volume of the inner shape is:", volume)

else:
    pyramid(axis=vector(0, 1, 1), color=color.yellow, opacity=0.3) ## Rectangular pyramid

''' ## Old turtle code that I couldn't figure out how to put into vpython terms
def plot_random_points(origin, number_of_points, size):
    for i in range(number_of_points):
        rand_x = randint(min(origin[0], origin[0] + size[0]), max(origin[0], origin[0] + size[0]))
        rand_y = randint(min(origin[1], origin[1] + size[1]), max(origin[1], origin[1] + size[1]))
        move_turtle((rand_x, rand_y))
        point.dot(point_size

plot_random_points((0,40),25)
'''