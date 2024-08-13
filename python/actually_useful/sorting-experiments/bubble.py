#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def bubble_sort(target_list: list[int | float]):
    target_list_ = target_list.copy()

    for sorted_count in range(len(target_list_)):
        swapped = False
        for i in range(len(target_list_) - sorted_count - 1):
            if target_list_[i] > target_list_[i+1]:
                target_list_[i], target_list_[i + 1] = target_list_[i + 1], target_list_[i]
                swapped = True
        if not swapped:  # the list is sorted
            break
    return target_list_


# length = random.randint(5, 10)
length = 100
list_to_sort = [random.randint(-100, 100) for a in range(length)]
print(list_to_sort)

sorted_ = bubble_sort(list_to_sort)
print(sorted_)

assert sorted_ == sorted(list_to_sort)
