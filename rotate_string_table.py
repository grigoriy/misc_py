def rotate(l, n):
    '''
    l: list of strings
    n: integer

    rotates table of strings in l clockwise n times
    
    returns: void
    '''
    for i in range(n):
        l = turn_table(l)


def turn_table(l):
	turned = []
	count = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
	for i in range(len(l[0])):
		turned.append('')
	for i in range(len(l)):
		print(count[i] + '\t', end='')
	print('\n')
	for i in range(len(l[0])):
		for s in range(len(l)-1, -1, -1):
			turned[i] += l[s][i]
			print(l[s][i], '\t', end='')
		print('\n')
	return turned
