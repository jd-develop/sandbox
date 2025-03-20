#!/usr/bin/env python3
# coding:utf-8

def negadecimal_to_decimal(negadecimal: int):
    assert negadecimal >= 0, "negadecimal values can’t be negative…"
    negadecimal_str = str(negadecimal)
    decimal = 0
    for i in range(1, len(negadecimal_str)+1):
        decimal += (-10)**(i-1) * int(negadecimal_str[-i])
    return decimal


def decimal_to_negadecimal(decimal_int: int):
    digits: list[int] = []
    while decimal_int != 0:
        r = decimal_int % (-10)
        decimal_int //= (-10)
        if r < 0:
            r += 10
            decimal_int += 1
        digits.append(r)
    negadecimal = 0
    for i in range(len(digits)):
        negadecimal += (10)**i * digits[i]
    return negadecimal



print(negadecimal_to_decimal(1901))
print(decimal_to_negadecimal(-99))

for i_ in range(-10000, 10000):
    assert negadecimal_to_decimal(decimal_to_negadecimal(i_)) == i_, f"{i_=}, {decimal_to_negadecimal(i_)}, {negadecimal_to_decimal(decimal_to_negadecimal(i_))}"

for i_ in range(20000):
    assert decimal_to_negadecimal(negadecimal_to_decimal(i_)) == i_
