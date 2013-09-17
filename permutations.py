def permutations(num):
    '''
    num: length of a set to be permutated
    '''
    if num == 0:
        return 1

    return permutations(num - 1) * num

def pow_set(num):
    '''
    num: length of a set, int

    returns: list of all subsets, list of ints
    '''
    result = {}

    for i in xrange(2 ** num):
        combo = 0
        for j in xrange(num):
            if (i >> j) % 2 == 1:
                combo += 1
        try:
            result[combo] += 1
        except KeyError:
            result[combo] = 1
    return result

def permut_pow_sets(num, low = None, hi = None):
    if low == None:
        low = 0
    if hi == None:
        hi = num
    result = 0
    pow_sets = pow_set(num)
    for x in pow_sets.iterkeys():
        if pow_sets[x] >= low and pow_sets[x] <= hi:
            result += permutations(x) * pow_sets[x]
    return result

num = int(raw_input('Enter a length of set to know the quantity of its permutations: '))
low = int(raw_input('Enter a low border: '))
hi = int(raw_input('Enter a hi border: '))

def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf

print pow_set(num)
permut_pow_sets = memoize(permut_pow_sets)
print permut_pow_sets(num, low, hi)
