# coding:utf-8
import random


def negadecimal_to_decimal(negadecimal: int):
    assert negadecimal >= 0, "negadecimal values can’t be negative…"
    negadecimal = str(negadecimal)
    decimal = 0
    for i in range(1, len(negadecimal)+1):
        decimal += (-10)**(i-1) * int(negadecimal[-i])
    return decimal


def decimal_to_negadecimal(decimal: int):
    # todo recoder avec des listes
    is_negative = decimal < 0
    decimal = str(decimal)
    if is_negative:
        decimal = decimal[1:]
    negadecimal = 0
    for i in range(1, len(decimal)+1):
        if is_negative:
            if (-10)**(i-1) > 0 and int(decimal[-i]) != 0:
                negadecimal += (20-int(decimal[-i])) * 10**(i-1)
            else:
                if len(str(negadecimal + 10**(i-1)*int(decimal[-i]))) > len(str(negadecimal)):
                    negadecimal += 10**(i-1)*int(decimal[-i])
                    # print(negadecimal)
                    negadecimal += (200 - negadecimal//(10**(i-1)))*10**(i-1)
                else:
                    negadecimal += 10**(i-1) * int(decimal[-i])
        else:
            if (-10)**(i-1) > 0:
                negadecimal += 10**(i-1) * int(decimal[-i])
            else:
                negadecimal += (20-int(decimal[-i])) * 10**(i-1)
    return negadecimal


print(negadecimal_to_decimal(1901))
print(decimal_to_negadecimal(-99))

for i_ in range(-10000, 10000):
    assert negadecimal_to_decimal(decimal_to_negadecimal(i_)) == i_, f"{i_=}, {decimal_to_negadecimal(i_)}, {negadecimal_to_decimal(decimal_to_negadecimal(i_))}"

for i_ in range(20000):
    assert decimal_to_negadecimal(negadecimal_to_decimal(i_)) == i_
