#!/usr/bin/env python3


def simp_frac(a, b):
    gcd = GCD(a, b)
    print((int)(a/gcd), "/", (int)(b/gcd))
    return ((int)(a/gcd), (int)(b/gcd))


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

simp_frac(a, b)
