import math
import random
import sys
import resource
import pylab

sys.setrecursionlimit(5000)

def cpu_time():
	return resource.getrusage(resource.RUSAGE_SELF)[0]


def num_pair_expr_1(X, a):
    '''
    X: sorted list of integers
    a: positive integer
    returns: integer, number of pairs of such indexes i,j, that sqrt(X[i]+X[j]) = a
    '''
    if type(a) != int or a < 0:
        raise TypeError('a should be a positive integer!')
    lenX = len(X)
    if lenX < 2:
        return 0
    counter = 0
##    cycles = 0
    cash = {}
    cash['prev'] = (sys.maxint, 0)
    under_root = a * a

    # Find such m, that m + m equals under_root (rounded to lower int)
    m = under_root / 2

    for i in xrange(lenX):
        if X[i] == cash['prev'][0]:
            counter += cash['prev'][1]
            break
        if X[i] > m:
            break
        for j in xrange(lenX - 1, i, -1):
##            cycles += 1
            pair = X[i] + X[j]
            if pair < a:
                break
            if pair == under_root:
                # print X[i], X[j]
                counter += 1
        cash['prev'] = (i, counter - cash['prev'][1])
##    print 'cycles =', cycles
    return counter

def num_pair_expr_2(X, a):
    '''
    X: sorted list of integers
    a: positive integer
    returns: integer, number of pairs of such indexes i,j, that sqrt(X[i]+X[j]) = a
    '''
    if type(a) != int or a < 0:
        raise TypeError('a should be a positive integer!')
    lenX = len(X)
    if lenX < 2:
        return 0
    counter = 0
##    cycles = 0

    # Find such int m, that square root of (m + m) equals a
    m = a*a/2

    for i in xrange(lenX):
        if X[i] > m:
            break
        for j in xrange(i + 1, lenX):
##            cycles += 1
            pair = X[i] + X[j]
            if pair < 0:
                continue
            pair_expr = math.sqrt(pair)
            if pair_expr == a:
                # print X[i], X[j]
                counter += 1
##    print 'cycles =', cycles
    return counter

def num_pair_expr_3(X, a):
    '''
    X: sorted list of integers
    a: positive integer
    returns: integer, number of pairs of such indexes i,j, that sqrt(X[i]+X[j]) = a
    '''
    if type(a) != int or a < 0:
        raise TypeError('a should be a positive integer!')
    lenX = len(X)
    if lenX < 2:
        return 0
    counter = 0
##    cycles = 0

    for i in xrange(lenX):
        for j in xrange(i + 1, lenX):
##            cycles += 1
            pair = X[i] + X[j]
            if pair < 0:
                continue
            pair_expr = math.sqrt(pair)
            if pair_expr == a:
                # print X[i], X[j]
                counter += 1
##    print 'cycles =', cycles
    return counter

def gen_list(length, a = -5000, b = 5000):
    '''
    length: integer, desired length of a generated list
    a, b: range of integers such, that a <= N <= b, in a generated list
    returns: a list of random integers of length n
    '''

    new_list = []
    for i in range(length):
        new_list.append(random.randint(a, b))

    return new_list

def merge_sort(l):
    '''
    l: list of integers
    returns: list, sorted in ascending order
    '''
    def merge(fir, sec, new = None):
        if new == None:
            new = []
        len_fir = len(fir)
        len_sec = len(sec)
        if len_fir == 0 and len_sec == 0:
            return new
        elif len_fir == 0 and len_sec != 0:
            new += sec
            sec = []
            return new
        elif len_sec == 0 and len_fir != 0:
            new += fir
            fir = []
            return new
        elif fir[0] <= sec[0]:
            new.append(fir.pop(0))
        else:
            new.append(sec.pop(0))
        return merge(fir, sec, new)

    if len(l) <= 1:
        return l

    first = l[0 : (len(l) / 2)]
    second = l[(len(l) / 2) : len(l)]
    return merge(merge_sort(first), merge_sort(second))

def test(a, lengths, start = -10000, end = 10000, numTrials = 500):
    '''
    a: positive integer
    lengths: list of integers, desired lengths of a generated list
    start, end: range of integers such, that a <= N <= b, in a generated list
    numTrials: positive integer

    returns: integer, number of pairs of such indexes i,j, that sqrt(X[i]+X[j]) = a
    '''
    func_dict = {}
    func_dict['gen'] = []
    func_dict['merge'] = []
    func_dict['find_1'] = []
    func_dict['find_2'] = []
    func_dict['find_3'] = []
    for length in lengths:
        times_gen = []
        times_merge = []
        times_find_1 = []
        times_find_2 = []
        times_find_3 = []
        for trial in xrange(numTrials):
            start_time = cpu_time()
            test_list = gen_list(length, start, end)
            times_gen.append(cpu_time() - start_time)
            start_time = cpu_time()
            sorted_list = merge_sort(test_list)
            times_merge.append(cpu_time() - start_time)
            start_time = cpu_time()
            result = num_pair_expr_1(sorted_list, a)
            times_find_1.append(cpu_time() - start_time)
            start_time = cpu_time()
            result = num_pair_expr_2(sorted_list, a)
            times_find_2.append(cpu_time() - start_time)
            start_time = cpu_time()
            result = num_pair_expr_3(sorted_list, a)
            times_find_3.append(cpu_time() - start_time)
        # func_dict['gen'].append(sum(times_gen) / len(times_gen))
        # func_dict['merge'].append(sum(times_merge) / len(times_merge))
        func_dict['find_1'].append(sum(times_find_1) / len(times_find_1))
        func_dict['find_2'].append(sum(times_find_2) / len(times_find_2))
        func_dict['find_3'].append(sum(times_find_3) / len(times_find_3))
    # pylab.plot(lengths, func_dict['gen'], 'bo-', label = 'gen')
    # pylab.plot(lengths, func_dict['merge'], 'go-', label = 'merge')
    pylab.plot(lengths, func_dict['find_1'], 'ro-', label = 'find_1')
    pylab.plot(lengths, func_dict['find_2'], 'yo-', label = 'find_2')
    pylab.plot(lengths, func_dict['find_3'], 'ko-', label = 'find_3')
    pylab.xticks(lengths)
    pylab.ylabel('Time taken, sec')
    pylab.xlabel('Number of items')
    pylab.legend(loc=0)
    pylab.show()

test(random.randint(0, 50), [25, 50, 100, 200, 300, 500, 1000])

# print num_pair_expr_1([1, 2, 5, 5, 5, 5, 5, 12, 13, 14, 15, 20, 25], 5), 'matches\n'
# print num_pair_expr_2([1, 2, 5, 5, 5, 5, 5, 12, 13, 14, 15, 20, 25], 5), 'matches\n'
# print num_pair_expr_3([1, 2, 5, 5, 5, 5, 5, 12, 13, 14, 15, 20, 25], 5), 'matches\n'
