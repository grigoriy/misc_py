#!/usr/bin/env python3

def GCD(a, b):
    if a >= b:
        r = a%b
        while r != 0:
            q = a//b
            r = a%b
            a = b
            b = r
        return a
    else:
        temp = a
        a = b
        b = temp
        return GCD(a,b)

a = int(input("type first number: "))
b = int(input("type second number: "))

print(GCD(a, b))
