from turtle import *

a1 = Turtle()
print(a1)
a1.shape("turtle")   #shapes ===> arrow', 'circle', 'classic', 'square', 'triangle', and 'turtle'
a1.color("aquamarine3")
a1.speed(10)
for i in range(20):
    for c in ("blue", "gold", "red"):
        a1.color(c)
        a1.forward(i)
        a1.right(30)

clearscreen()
a1.setposition(0,0)
a1.fillcolor("gold")
a1.begin_fill()
while True:
    a1.forward(200)
    a1.left(170)
    if abs(a1.pos()) < 1:
        break

a1.end_fill()


sc = Screen()
print(sc.canvheight)

sc.exitonclick()