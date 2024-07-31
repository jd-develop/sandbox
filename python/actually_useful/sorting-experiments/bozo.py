#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def bozo_sort(target_list: list[int | float]):
    target_list_ = target_list.copy()

    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i, e in enumerate(target_list_):
            if i != 0 and e < target_list_[i-1]:
                is_sorted = False
                break
        if not is_sorted:
            random.shuffle(target_list_)

    return target_list_


# length = random.randint(5, 10)
length = 4
list_to_sort = [random.randint(-100, 100) for a in range(length)]
print(list_to_sort)

sorted_ = bozo_sort(list_to_sort)
print(sorted_)

assert sorted_ == sorted(list_to_sort)
