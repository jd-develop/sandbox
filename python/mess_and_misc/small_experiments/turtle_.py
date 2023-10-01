#!/usr/bin/env python3
# coding:utf-8
# my first turtle program
import turtle
from random import choice

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

turtle1.width(5)
turtle2.width(5)
turtle3.width(5)

turtle1.color(choice(colors))
turtle2.color(choice(colors))
turtle3.color(choice(colors))

turtle1.up()
turtle2.up()
turtle3.up()
turtle1.goto(-100, -100)
turtle2.goto(0, -100)
turtle3.goto(-50, -13.4)
turtle1.down()
turtle2.down()
turtle3.down()

a = 100
for loop in range(2):
    for loop2 in range(3):
        turtle1.forward(a)
        turtle1.left(120)
        turtle2.forward(a)
        turtle2.left(120)
        turtle3.forward(a)
        turtle3.left(120)
        turtle1.color(choice(colors))
        turtle2.color(choice(colors))
        turtle3.color(choice(colors))
    a = 50

turtle1.forward(50)
turtle2.forward(50)
turtle3.forward(50)

for loop in range(5):
    turtle1.forward(a)
    turtle1.left(120)
    turtle2.forward(a)
    turtle2.left(120)
    turtle3.forward(a)
    turtle3.left(120)
    turtle1.color(choice(colors))
    turtle2.color(choice(colors))
    turtle3.color(choice(colors))

turtle1.right(60)
turtle2.right(60)
turtle3.right(60)
turtle1.forward(50)
turtle2.forward(50)
turtle3.forward(50)

turtle1.up()
turtle2.up()
turtle3.up()
turtle1.goto(500, 0)
turtle2.goto(500, 0)
turtle3.goto(500, 0)

turtle.exitonclick()