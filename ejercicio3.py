def count_times(a, b):
    '''This function count the times that b is in a list
    b is an item and a is a list'''
    c = 0
    for d in a:
        if d == b:
            c += 1
    return c

print(count_times([1, 2, 3, 5, 2, 7, 2, 2], 2))
