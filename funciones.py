def a(b):
    c = None
    while c == None:
        try:
            c = input(b).upper()
            if len(c) < 6:
                print('Error')
                c = None
        except:
            print('Error')
    return c


def b(c, d):
    e = 0
    for f in c:
        try:
            if f == d:
                e += 1
        except:
            print('Error')
            e = 0
    return e

def c(d, e, f):
    g = None
    while g == None:
        try:
            g = int(input(d))
            if g < e or g > f:
                print('Error')
                g = None
        except:
            print('Error')
    return g

def d(e, f):
    if e == 0:
        return e
    else:
        return f + d(e-1,f)
