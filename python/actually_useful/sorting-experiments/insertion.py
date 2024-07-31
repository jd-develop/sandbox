#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def insertion_sort(target_list: list[int | float]):
    target_list_ = target_list.copy()

    for i in range(1, len(target_list_)):
        j = i
        while j > 0 and target_list_[j-1] > target_list_[j]:
            target_list_[j], target_list_[j-1] = target_list_[j-1], target_list_[j]
            j -= 1

    return target_list_


def felix_insertion_sort(lst):
    """Felix' insertion sort — thanks Felix!"""
    lst = lst.copy()
    for i in range(len(lst)):
        insert_char(lst, i, lst[i])
    return lst


def insert_char(lst, i, v):
    j = i
    while j > 0 and lst[j-1] > v:
        lst[j] = lst[j-1]
        j = j-1
    lst[j] = v


# length = random.randint(5, 10)
length = 100
list_to_sort = [random.randint(-1000, 9999) for a in range(length)]
print(list_to_sort)

sorted_ = insertion_sort(list_to_sort)
print(sorted_)

assert sorted_ == sorted(list_to_sort) == felix_insertion_sort(list_to_sort)
