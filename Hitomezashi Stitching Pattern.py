## A random Hitomezashi stitching pattern is made with each run! I colored the pattern orange for fun. :-)

import tkinter as tk
from tkinter import Canvas
import random, math

class Pattern(tk.Tk):

    def generate_numbers(self):
        ## Create two arrays of numbers of a given length
        self.horizontal_numbers = []
        self.vertical_numbers = []

        for horizontal in range(0, self.horizontal_line_length):
            self.horizontal_numbers.append(random.randrange(0,2))

        for vertical in range(0, self.vertical_line_length):
            self.vertical_numbers.append(random.randrange(0,2))

    ## If the number is odd, the line will be offset.. if even, start at the start of the line, which is at 0
    ## (this is the rule we are following)
    def create_pattern(self):
        for index, value in enumerate(self.vertical_numbers):
            if value % 2 == 0:
                self.dashed_vertical_line(index*10,0)
            else:
                self.dashed_vertical_line(index*10,10)

        for index, value in enumerate(self.horizontal_numbers):
            if value % 2 == 0:
                self.dashed_horizontal_line(index*10,0)
            else:
                self.dashed_horizontal_line(index*10,10)

    ## The dashed methods account for the lines drawn and the amount of space in-between the lines
    def dashed_horizontal_line(self, depth, start):
        for i in range(0, int(self.vertical_line_length/2)):
            points = [
                start,
                depth,
                start + 10,
                depth
            ]
            self.canvas.create_line(points, fill = "#FF8724", width = 3)
            start = start + 20

    def dashed_vertical_line(self, depth, start):
        for i in range(0, int(self.horizontal_line_length/2)):
            points = [
                depth,
                start,
                depth,
                start + 10
            ]
            self.canvas.create_line(points, fill = "#FF8724", width = 3)
            start = start + 20

    ## The geometry of the top level window is set to match the horizontal and vertical lengths of the arrays
    def resize_window(self):
        toplevelwindow = self.winfo_toplevel()
        toplevelwindow.wm_geometry(str(self.vertical_line_length * 10) + "x" + str(self.horizontal_line_length * 10))

    ## Constructor
    def __init__(self, horizontal=30, vertical=30):
        super().__init__() ## Without this, there is a recursion error

        self.horizontal_line_length = horizontal
        self.vertical_line_length = vertical

        self.title("Hitomezashi Stitching Pattern")

        ## This makes users unable to resize the window
        self.resizable(False, False)

        ## Creating the canvas widget
        self.canvas = Canvas(background="#FFD16A")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        ## Using the methods that we made
        self.generate_numbers()
        self.create_pattern()
        self.resize_window()

## Main driver
if __name__ == "__main__":
    canvas = Pattern(55,90) ## Length and width of window
    canvas.mainloop()