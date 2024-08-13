#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def merge_sort(target_list: list[int | float]):
    target_list_ = target_list.copy()

    if len(target_list_) == 1:
        return target_list_
    middle_i = len(target_list_) // 2
    array_left = merge_sort(target_list_[:middle_i])
    array_right = merge_sort(target_list_[middle_i:])
    target_list_ = merge(array_left, array_right)

    return target_list_


def merge(array1, array2):
    array_final = [0]*(len(array1) + len(array2))
    i = j = k = 0  # `i` is index in array1, `j` in array2 and `k` in array_final
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            array_final[k] = array1[i]
            i += 1
        else:
            array_final[k] = array2[j]
            j += 1
        k += 1

    while i < len(array1):
        array_final[k] = array1[i]
        i += 1
        k += 1

    while j < len(array2):
        array_final[k] = array2[j]
        j += 1
        k += 1

    return array_final


# length = random.randint(5, 10)
length = 100
list_to_sort = [random.randint(-1000, 9999) for a in range(length)]
print(list_to_sort)

sorted_ = merge_sort(list_to_sort)
print(sorted_)

assert sorted_ == sorted(list_to_sort)
