def f(a):
    b = 0  # this can change
    for c in range(1, a):
        if a % c == 0:  # this can change
            b += c  # this can change
    print(c)
    return a - b == 0

print(f(4))
