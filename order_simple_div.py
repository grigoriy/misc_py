def num_in_div_order(n, n_range):
    '''
    n: positive integer
    n_range: positive integer

    returns: place of n in a list of range [1, n_range] sorted by divisibility
    by simple numbers (acsending)
    '''

    simple = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    normal = []
    new_order = []
    for num in xrange(1, n_range + 1):
        normal.append(num)
    
    for simple in simple:
        len_norm = len(normal)
        temp = []
        count = 0
        if len_norm == 0:
            break
        for i in xrange(len_norm):
            num = normal[i]
            if num % simple == 0:
                new_order.append(num)
                temp.append(num)
                count += 1
                if num == n:
                    return len(new_order)
        print count
        for num in temp:
            normal.remove(num)
