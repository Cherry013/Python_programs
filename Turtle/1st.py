from turtle import *

Curse = Turtle()
Curse.shape("turtle")
Curse.color("black")

Curse.backward(50)
Curse.forward(100)
for i in range(4):
    Curse.left(90)
    Curse.forward(100)

Screen().exitonclick()
# mainloop()
