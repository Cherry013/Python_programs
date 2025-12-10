import turtle as t
import random

spi = t.Turtle()
t.colormode(255)

def rgb():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

spi.speed("fastest")

def spirograph(size_of_the_gap):
    for _ in range(360//size_of_the_gap):
        spi.color(rgb())
        spi.circle(100)
        spi.setheading(spi.heading() + size_of_the_gap)


spirograph(1)

screen = t.Screen()
screen.exitonclick()