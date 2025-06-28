import turtle
from turtle import *

screen = turtle.Screen()
screen.title("Tiranga")

flag = turtle.Turtle()
flag.speed('fastest')
flag.hideturtle()  

flag.penup()
flag.goto(-120, 125)
flag.pendown()

flag.color("orange")
flag.begin_fill()
flag.forward(400)
flag.right(90)
flag.forward(84)
flag.right(90)
flag.forward(400)
flag.end_fill()

flag.left(90)
flag.forward(84)

flag.color("green")
flag.begin_fill()
flag.forward(84)
flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(84)
flag.end_fill()

flag.penup()
flag.goto(115, 0)
flag.pendown()
flag.color("navy")
flag.begin_fill()
flag.circle(35)
flag.end_fill()

flag.penup()
flag.goto(110, 0)
flag.pendown()
flag.color("white")
flag.begin_fill()
flag.circle(30)
flag.end_fill()

flag.penup()
flag.goto(54, -4)
flag.pendown()
flag.color("navy")
for j in range(24):
    flag.begin_fill()
    flag.circle(2)
    flag.end_fill()
    flag.penup()
    flag.forward(7)
    flag.right(15)

flag.penup()
flag.goto(90, 0)
flag.pendown()
flag.begin_fill()
flag.circle(10)
flag.end_fill()

flag.penup()
flag.goto(80, 0)
flag.pendown()
flag.pensize(1)
for j in range(24):
    flag.forward(30)
    flag.backward(30)
    flag.left(15)

flag.color("brown")
flag.pensize(10)
flag.penup()
flag.goto(-120, 125)
flag.setheading(-90)
flag.pendown()
flag.forward(500)

turtle.done()