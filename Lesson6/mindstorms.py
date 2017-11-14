import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("blue")
    brad.turtlesize(5,5,12)
    brad.speed(5)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(200)
    brad.right(90)

    window.exitonclick()

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("blue")

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)
    window.exitonclick()

draw_square()
draw_circle()