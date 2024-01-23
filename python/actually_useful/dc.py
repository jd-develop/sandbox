#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
A very simple reverse-polish notation calculator
"""
import sys
from typing import Literal
try:
    import readline  # type: ignore
except ImportError:
    pass
import math


def is_num(command: str, can_start_with_minus: bool = True) -> tuple[bool, Literal["float", "int"] | None]:
    if command == "-":
        return False, None
    if command.startswith("-") and can_start_with_minus:
        return is_num(command[1:], False)
    if command.isnumeric():
        return True, "int"
    command_list = command.split(".")
    if len(command_list) != 2:
        return False, None
    if command_list[0].isnumeric() and command_list[1].isnumeric():
        return True, "float"
    return False, None



stack: list[int | float] = []
print_last_stack_value = True
while True:
    user_input = input("dc> ")
    if user_input == "" or set(user_input) == set(" "):
        continue
    
    old_stack = stack.copy()
    error = False
    just_printed = False
    for word in user_input.split():
        is_numeric, num_type = is_num(word)
        if is_numeric:
            if num_type == "int":
                stack.append(int(word))
            else:
                stack.append(float(word))
        elif word == "e":
            stack.append(math.e)
        elif word == "pi":
            stack.append(math.pi)
        elif word == "+":
            if len(stack) < 2:
                print("Error: not enough numbers to perform '+'")
                error = True
                continue
            b, a = stack.pop(), stack.pop()
            stack.append(a+b)
        elif word == "-":
            if len(stack) < 2:
                print("Error: not enough numbers to perform '-'")
                error = True
                continue
            b, a = stack.pop(), stack.pop()
            stack.append(a-b)
        elif word == "*":
            if len(stack) < 2:
                print("Error: not enough numbers to perform '*'")
                error = True
                continue
            b, a = stack.pop(), stack.pop()
            stack.append(a*b)
        elif word in ["**", "^"]:
            if len(stack) < 2:
                print(f"Error: not enough numbers to perform '{word}'")
                error = True
                continue
            b, a = stack.pop(), stack.pop()
            stack.append(a**b)
        elif word in ["%", "mod"]:
            if len(stack) < 2:
                print(f"Error: not enough numbers to perform '{word}'")
                error = True
                continue
            b, a = stack.pop(), stack.pop()
            try:
                stack.append(a%b)
            except ZeroDivisionError:
                print("Error: division by zero")
                error = True
        elif word == "//":
            if len(stack) < 2:
                print(f"Error: not enough numbers to perform '//'")
                error = True
                continue
            b, a = stack.pop(), stack.pop()
            try:
                stack.append(a//b)
            except ZeroDivisionError:
                print("Error: division by zero")
                error = True
        elif word == "/":
            if len(stack) < 2:
                print("Error: not enough numbers to perform '/'")
                error = True
            b, a = stack.pop(), stack.pop()
            try:
                stack.append(a/b)
            except ZeroDivisionError:
                print("Error: division by zero")
                error = True
        elif word == "sqrt":
            if len(stack) == 0:
                print("Error: not enough numbers to perform 'sqrt'")
                error = True
                continue
            if stack[-1] < 0:
                print("Error: negative numbers do not have a square root.")
                error = True
                continue
            number = stack.pop()
            stack.append(math.sqrt(number))
        elif word in ["log", "loge", "ln", "le", "l"]:
            if len(stack) == 0:
                print(f"Error: not enough numbers to perform '{word}'")
                error = True
                continue
            number = stack.pop()
            stack.append(math.log(number))
        elif word in ["log10", "l10"]:
            if len(stack) == 0:
                print(f"Error: not enough numbers to perform '{word}'")
                error = True
                continue
            number = stack.pop()
            stack.append(math.log10(number))
        elif word in ["log2", "l2"]:
            if len(stack) == 0:
                print(f"Error: not enough numbers to perform '{word}'")
                error = True
                continue
            number = stack.pop()
            stack.append(math.log2(number))
        elif word in ["logb", "logbase", "lb"]:
            if len(stack) == 0:
                print(f"Error: not enough numbers to perform '{word}'")
                error = True
                continue
            base = stack.pop()
            number = stack.pop()
            stack.append(math.log(number, base))
        elif word in ["c", "clear"]:
            print("Stack cleared")
            stack = []
        elif word in ["exit", "done", "quit", "q"]:
            print("Bye.")
            sys.exit(0)
        elif word in ["s", "stack"]:
            just_printed = True
            print(" ".join(map(str, stack)))
        elif word in ["p", "print"]:
            if len(stack) >= 1:
                print(stack[-1])
                just_printed = True
            else:
                print("Stack is empty.")
        elif word in ["sp", "switchprint"]:
            print_last_stack_value = not print_last_stack_value
            if print_last_stack_value:
                print("I will now print the last value in the stack automatically.")
            else:
                print("Ok, the last value in the stack will no longer be printed.")
        else:
            print(f"Error: unrecognised command: '{word}'")
            error = True
    
    if error:
        print("Stack is unchanged.")
        stack = old_stack

    if len(stack) >= 1 and print_last_stack_value and not error and not just_printed:
        print(stack[-1])
