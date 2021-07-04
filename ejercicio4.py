def r(a):
    '''a is a list and b stores the product of all the items'''
    b = 1
    for c in a:
        b *= c
    return b


def y(a):
    '''a is a list and b stores the sum of all the items'''
    b = 0
    for c in a:
        b += c
    return b


print(r([1, 2, 3]))
print(y([4, 5, 6]))
