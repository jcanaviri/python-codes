def z(a):
    '''Returns all the divisors of a'''
    b = []
    for c in range(a):
        if a % (c + 1) == 0:
            b.append(c + 1)
    return b


print(z(2))
print(z(3))
print(z(5))

print(z(10))
print(z(15))
print(z(25))
