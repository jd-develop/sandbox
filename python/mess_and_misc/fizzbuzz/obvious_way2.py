#!/usr/bin/env python3
# -*- coding:utf-8 -*-

for i in range(1, 101):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"

    if result == "":
        result = i

    print(result)
