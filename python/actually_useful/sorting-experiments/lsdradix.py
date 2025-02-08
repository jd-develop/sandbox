#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from math import log2

def lsdradix(t: list[int], poweroftwo: int = 0, maxpower: int = 0) -> list[int]:
    if maxpower == 0:
        for i in t:
            exp = int(log2(i))
            if exp > maxpower:
                maxpower = exp
        assert maxpower > 0
    if poweroftwo > maxpower:
        return t

    t0: list[int] = []
    t1: list[int] = []
    for i in t:
        if (i >> poweroftwo) % 2 == 0:
            t0.append(i)
        else:
            t1.append(i)

    return lsdradix(t0+t1, poweroftwo+1, maxpower)
