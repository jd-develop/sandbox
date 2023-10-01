#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from itertools import product

possibilities = 0
for list_ in product(*[range(10)] * 3):
    print(list_)
    possibilities += 1
print(possibilities)
