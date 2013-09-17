#!/usr/bin/env python3


def factorial(n):
    if n < 0:
        return "Input must be a non-negative integer!"
    elif n < 2:
        return 1
    return n * factorial(n-1)



while True:
    n = input("Type positive integer get its factorial or 'q' to quit: ")
    if n == 'q':
        break
    print(factorial(int(n)))
