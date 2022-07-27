def common_items(a, b):
    '''This function returns all the common elements 
    in both list a and b'''
    c = []
    for d in range(len(a)):
        for e in range(len(b)):
            if a[d] == b[e]:
                c.append(a[d])
                b = b[:e] + b[e+1:]
                break
    return c


print(common_items([1, 2, 3], [4, 2, 3]))
