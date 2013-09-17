#!usr/bin/env python

def wrapper(s, moves=moves, mod=3, path=None):
    initial = str_to_grid(s)
    raw = solve_m(initial, moves, mod, path)
    return tuple(moves_dict[vect] for vect in raw)


solve_m = memoize(solve)


def solve(initial, moves, mod=None, path=None):
    '''
    initial: list of 9 ints in range[0,1,2], initial grid
    moves: list of lists of ints in range[0,1,2], possible moves in the game
    mod: int, modulo
    path: list of moves been made

    returns: tuple of ints(numbers of boxes needed to be touched to solve puzzle)
    '''
    if path is None:
        path = []
   
    for i in range(1, len(initial)):
        if initial[i] != initial[i - 1]:
            break
    else:
        return path

    if len(moves) < 1:
        return None

    first = moves[0]
    try:
        rest = moves[1:]
    except:
        rest = ()
    sum_1 = vec_add(initial, first, mod)
    path_1 = path + [first]
    var_1 = solve(sum_1, rest, mod, path_1)
    var_2 = solve(initial, rest, mod, path)

    return var_1 if var_2 is None else var_2


def vec_add(a, b, mod=None):
    '''
    a, b: iterables of equal length, vectors

    returns: sum of a & b
    '''
    if mod is None:
        return tuple((x + y) for (x, y) in zip(a, b))
    else:
        return tuple((x + y) % mod for (x, y) in zip(a, b))


def str_to_grid(s):
    '''
    s: string of 9 characters, each of which is either 'w', or 'b', or 'r'

    returns: tuple of 9 ints in range[0,1,2]
    '''
    result = []
    for letter in s:
        if letter == 'w':
            result.append(0)
        elif letter == 'b':
            result.append(1)
        elif letter == 'r':
            result.append(2)
        else:
            raise ValueError('Only w,b,r allowed!')
    return tuple(result)


def memoize(f):
    # define "wrapper" function that checks cache for
    # previously computed answer, only calling f if this
    # is a new problem.
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf


## Hard-coded data ##

# Possible moves
m1 = '110100000'
m2 = '111000000'
m3 = '011001000'
m4 = '100100100'
m5 = '010111010'
m6 = '001001001'
m7 = '000100110'
m8 = '000000111'
m9 = '000001011'

temp_moves = (m1, m1, m2, m2, m3, m3, m4, m4, m5, m5, m6, m6, m7, m7,
              m8, m8, m9, m9)

moves = tuple(tuple(int(x) for x in m) for m in temp_moves)

moves_dict = {vect: cell for cell, vect in zip(range(1, 10), moves[::2])}
