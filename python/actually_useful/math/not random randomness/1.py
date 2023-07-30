#!/usr/bin/env python3
# coding:utf-8
# https://www.youtube.com/watch?v=2Wq6H8GMVm0
import turtle as tl
import random

steps = 50

tl.setworldcoordinates(0, -200, 500, 200)
t = tl.Turtle()
t.pendown()
for step in range(steps):
    t.setheading(random.choice([25, -25]))
    t.forward(500/steps)

tl.mainloop()
