#!/usr/bin/env python3
'''
computes number of combinations "n choose k"
'''

def comb(n, k):
    from math import factorial
    return int((factorial(n) / (factorial(n-k) * factorial(k))))


n = input("Enter n: ")
k = input("Enter k: ")
print(comb(int(n), int(k)))
