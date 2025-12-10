from turtle import *

line = Turtle()
title("Dashed Line")
line.shape("arrow")
line.color("green")

for i in range(8):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()

mainloop()