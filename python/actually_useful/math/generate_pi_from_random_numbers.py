# coding:UTF-8
# The probability of two random numbers to be coprime is 6/(π²)
import math
import random


def gcd(a, b):
    """Return the GCD (greatest common divisor) of a and b with the Euclides algorithm."""
    if b == 0:
        return abs(a)
    if a == 0:
        return abs(b)
    next_a = a
    next_b = b
    while next_b != 0:
        next_a, next_b = next_b, next_a % next_b
    return next_a


def are_co_primes(a, b):
    """Return True if their GCD is 1"""
    return gcd(a, b) == 1


co_primes = 0
total = 0
for i in range(1000000):
    random1 = random.randint(1, 10000)
    random2 = random.randint(1, 10000)
    if are_co_primes(random1, random2):
        co_primes += 1
    total += 1


print(f"{co_primes=}")
print(f"{total=}")
print(f"{co_primes/total=}, 6/(π²)={6/(math.pi**2)}")
print()

pi = math.sqrt(total*6/co_primes)
print(f"We found π={pi}.\nThe real π={math.pi}")
