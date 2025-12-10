from turtle import *

shapes = Turtle()

shapes.penup()
shapes.goto(-50,-100)
shapes.pendown()

title("Shapes")
shapes.color("red")
def draw_shape(num_sides):
    for i in range(num_sides):
        shapes.forward(100)
        angle = 360/num_sides
        shapes.left(angle)

for i in range(3,11):
    #shapes.color("color name")
    draw_shape(i)

# for i in range(4):
#     shapes.forward(100)
#     shapes.left(90)
# shapes.right(45)
# shapes.forward(80)
# shapes.left(97)
# shapes.forward(72)

# shapes.penup()
# shapes.left(128)
# shapes.forward(250)
# shapes.pendown()

# for i in range(5):
#     shapes.forward(75)
#     shapes.left(72)

# for i in range(6):
#     shapes.forward(75)
#     shapes.right(60)


Screen().exitonclick()