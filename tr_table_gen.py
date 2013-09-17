def ttable(n):
    '''
    n: positive integer, number of propositional vars

    prints a truth table of n propositional vars

    returns 0 if successful
    '''
    def helper(n, row = None, result = None):
        if row == None:
            row = []
        if result == None:
            result = []
        if n < 1:
            result.append(row)
            return result

        new = list(row)
        new.append(1)
        row.append(0)
        first = helper(n-1, new, result)
        second = helper(n-1, row, result)

        return second

    return helper(n)

def print_table(table, col_names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    '''
    table: list of lists
    col_names: iterable sequence of column names

    prints a table to stdout
    '''
    for var in xrange(n):
        print col_names[var], ' ',
    print '\n', '-'*(4*n - 1)
    for row in result:
        for col in row:
            print col, '|',
        print ''    
