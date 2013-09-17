import operator

def mergeSort(L, x, compare = operator.lt):
    x += 1
    if len(L) < 2:
        print ("   "*x + "Exit MergeSort")
        return L[:]
    else:
        middle = int(len(L)/2)
        print ("   "*x + "Enter MergeSort Left: " + str(L[:middle]))
        left = mergeSort(L[:middle], x, compare)
        print ("   "*x + "Enter MergeSort Right: " + str(L[middle:]) )
        right = mergeSort(L[middle:], x , compare)
        print ("   "*x + "Enter Merge: Left= " +str(left) + " Right=" + str(right))
        return merge(left, right, compare, x)

def merge(left, right, compare, x):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print ("   "*x + "Exit Merge: Result= "+ str(result))
    return result
