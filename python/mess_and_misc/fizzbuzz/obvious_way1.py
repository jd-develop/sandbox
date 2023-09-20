#!/urs/bin/env python3
# -*- coding:utf-8 -*-

for i in range(1, 101):
    is_divisible_by_3 = i%3 == 0
    is_divisible_by_5 = i%5 == 0
    if is_divisible_by_3 and is_divisible_by_5:
        print("FizzBuzz")
    elif is_divisible_by_3:
        print("Fizz")
    elif is_divisible_by_5:
        print("Buzz")
    else:
        print(i)

