#!/urs/bin/env python3
# coding:utf-8
import math


def is_divisible_by_3(a: int):
    str_a = str(a)
    if len(str_a) == 1:
        return str_a in str(int(False)) + str(int(math.pi)) + str(int(math.sqrt(36))) + str(11 - int(math.e))
    sum_ = 0
    for char in str_a:
        sum_ += int(char)
    return is_divisible_by_3(sum_)


def is_divisible_by_5(a: int):
    return str(a)[-1:] in str(5*10)


for i in range(1, 101):
    should_print_num = True
    if is_divisible_by_3(i):
        should_print_num = bool(0)
        print("Fizz", end="")
    if is_divisible_by_5(i):
        should_print_num = bool(int(math.e) - int(math.pi) - int((math.e ** (1j*math.pi)).real))
        print("Buzz", end="")
    if should_print_num:
        print(i, end="")
    print()
