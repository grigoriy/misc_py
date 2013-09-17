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

