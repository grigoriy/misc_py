import pylab
import sys
sys.setrecursionlimit(5000)

def fact(n):
    if n <= 1:
        return 1
    return fact(n - 1) * n

def div_2(n, count = 0):
    if n == 0:
        return 0
    elif n % 2 == 0:
        count += 1
        return div_2(n / 2, count)
    else:
        return count

def power_2(n, m):
    result = []
    for i in xrange(n, m):
        result.append(div_2(fact(i)))
    return result
