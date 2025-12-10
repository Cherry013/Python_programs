import turtle as t
import random

ran = t.Turtle()
t.colormode(255)
def rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    k = (r, g, b)
    return k

#col = ['red','green','blue','indianred','firebrick','ForestGreen','CornFlowerBlue','DarkOrchid']
Directions = [0,90,180,270]

ran.pensize(8)
for i in range(200):
    ran.color(rgb())
    ran.forward(50)
    ran.setheading(random.choice(Directions))