#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# This software is licensed under the WTFPL
"""
Turns out if you flip a coin until you get more heads than tails, the expectancy
of 4heads/tails is π!
"""
import random


def sequence_of_flips() -> float:
    heads = 0
    tails = 0
    while heads <= tails and heads+tails <= 100000:
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    return 4 * (heads/(tails+heads))


def montecarlo(n: int) -> float:
    sum_ = 0
    for i in range(n):
        print(i)
        sum_ += sequence_of_flips()
    return sum_/n


print(montecarlo(100000))

