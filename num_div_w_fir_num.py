def find_div(n):
    '''
    n: positive integer

    returns: integer, number of such natural divisors of n, that their first number equals first number of n
    '''
    # find the first number of n
    if n < 1:
        raise ValueError('n must be a positive integer!')
    result = 1
    if n < 10:
        return result
    order = 0
    first = n
    half = n / 2
    while True:
        first = first / 10
        order += 1
        if first < 10:
            break

    print 'First:', first, 'Order:', order

    for i in xrange(order):
        start = 10 ** i * first
        end = start + 10 ** i
        for j in xrange(start, end):
            if j > half:
                return result
            elif n % j == 0:
                print j
                result += 1
    print n
    print 'Result:', result

    return result

def interact():
    while True:
        prompt = raw_input('To start an application, type Y, to quit - type N: ').lower()
        if prompt == 'y':
            find_div(int(raw_input('Type a positive integer: ')))
        elif prompt == 'n':
            break
        else:
            print 'Invalid input!'
            interact()

interact()
