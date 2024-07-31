#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
"""Timsort is the default algorithm built-in in python -- in the sorted() method."""

RUN = 32


def insertion_sort(target_list: list[int | float], start_i=None, end_i=None):
    if start_i is None:
        start_i = 0
    if end_i is None:
        end_i = len(target_list)

    for i in range(1+start_i, 1+end_i):
        j = i
        while j > start_i and target_list[j-1] > target_list[j]:
            target_list[j], target_list[j-1] = target_list[j-1], target_list[j]
            j -= 1


def timsort(target_list: list[int | float]):
    target_list_ = target_list.copy()

    for start_i in range(0, len(target_list_), RUN):
        end = min(start_i + RUN - 1, len(target_list_)-1)
        insertion_sort(target_list_, start_i, end)

    # we merge sub-arrays that have a size of 32 then 64, 128, 256, ...
    size = RUN
    n = len(target_list_)
    while size < n:
        for left in range(0, n, 2*size):
            mid = min(n-1, left+size-1)
            right = min(n-1, left + 2*size - 1)

            if mid < right:
                target_list_ = merge(target_list_, left, mid, right)
        size *= 2
    return target_list_


def merge(array, left, mid, right):
    len1, len2 = mid-left+1, right-mid
    left_list, right_list = array[left:mid], array[mid:right]
    assert len(left_list) == len1, f"{len(left_list)=} {len1=}"
    assert len(right_list) == len2, f"{len(right_list)=} {len2=}"
    i, j, k = 0, 0, left  # `i` is index in first part, `j` in second part and `k` in whole array
    while i < len1 and j < len2:
        if left_list[i] <= right_list[j]:
            array[k] = left_list[i]
            i += 1
        else:
            array[k] = right_list[j]
            j += 1
        k += 1

    while i < len1:
        array[k] = left_list[i]
        i += 1
        k += 1

    while j < len2:
        array[k] = right_list[j]
        j += 1
        k += 1
    return array


# length = random.randint(5, 10)
length = 100
list_to_sort = [random.randint(-1000, 9999) for a in range(length)]
print(list_to_sort)

sorted_ = timsort(list_to_sort)
print(sorted_)

assert sorted_ == sorted(list_to_sort)
