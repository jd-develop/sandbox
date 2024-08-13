#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def selection_sort(target_list: list[int | float]):
    target_list_ = target_list.copy()

    for start_i in range(len(target_list_)):
        # check for the lowest value's index in the list
        lowest_i = start_i
        for check_i in range(start_i + 1, len(target_list_)):
            if target_list_[check_i] < target_list_[lowest_i]:
                lowest_i = check_i

        target_list_[start_i], target_list_[lowest_i] = target_list_[lowest_i], target_list_[start_i]

    return target_list_


def selection_sort_fast(target_list: list[int | float]):
    target_list_ = target_list.copy()

    for start_i in range(len(target_list_)):
        check_list = target_list_[start_i:]
        lowest_i = check_list.index(min(check_list)) + start_i
        target_list_[start_i], target_list_[lowest_i] = target_list_[lowest_i], target_list_[start_i]

    return target_list_


# length = random.randint(5, 10)
length = 100
list_to_sort = [random.randint(-1000, 9999) for a in range(length)]
list_to_sort.insert(random.choice(list_to_sort), random.randint(0, len(list_to_sort)-1))
print(list_to_sort)

sorted_ = selection_sort(list_to_sort)
print(sorted_)

fast_sorted = selection_sort_fast(list_to_sort)
print(fast_sorted)
print(sorted_ == fast_sorted)

assert sorted_ == fast_sorted == sorted(list_to_sort)
