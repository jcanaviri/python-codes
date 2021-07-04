def t(a):
    # Los primos que multiplicados da 'a'
    b = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    c = 0
    d = []
    while a != 1:
        if a % b[c] == 0:
            a //= b[c]
            d.append(b[c])
        else:
            c += 1
    return d


def u(a, b):
    # Listas a y b crea c con los elementos comunes
    c = []
    for d in range(len(a)):
        for e in range(len(b)):
            if a[d] == b[e]:
                c.append(a[d])
                b = b[:e] + b[e+1:]
                break
    return c


def v(a, b):
    # Si el elemento b esta en a
    c = 0
    for d in a:
        if d == b:
            c += 1
    return c

def x(a):
    # Multiplica los elementos de la lista
    b = 1
    for c in a:
        b *= c
    return b

def y(a):
    # Suma los elementos de la lista
    b = 0
    for c in a:
        b += c
    return b
     
def z(a):
    b = []
    for c in range(a):
        if a % (c + 1) == 0:
            b.append(c + 1)
    return b
