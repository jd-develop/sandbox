#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# this program implements a pseudo-code algorithm that we wrote as math homework
import math


def f(x: int | float):
    return (math.e**x)/(1+x)


p = int(input("Entrez p : "))
n = (math.e-2)/(2*10**-p)
n = int(n) + 1
print(f"{n=}")
s = 0
for k in range(n):
    s += f(k/n)
print(s/n)
