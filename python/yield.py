#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def generator():
    a = 1
    while True:
        yield a*2
        a += 1


for i in generator():
    if i > 10:
        break
    print(i)
