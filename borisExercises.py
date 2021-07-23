def prime_factors(num):
    '''This function takes a number "num" and returns its prime factors'''
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    i = 0
    divisors = []
    while num != 1:
        # if num is divisible by a prime
        if num % primes[i] == 0:
            num //= primes[i]
            divisors.append(primes[i])
        else:
            i += 1
    return divisors


print(prime_factors(25))


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


def count_times(a, b):
    '''This function count the times that b is in a list
    b is an item and a is a list'''
    c = 0
    for d in a:
        if d == b:
            c += 1
    return c


print(count_times([1, 2, 3, 5, 2, 7, 2, 2], 2))


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


def count_words(string):
    words = string.split(' ')
    words_dict = {}
    for word in words:
        words_dict.setdefault(word.lower(), 0)
        words_dict[word.lower()] += 1
    return words_dict


def most_common(word_dict):
    value = 0
    key = None
    for k, v in word_dict.items():
        if v > value:
            value = v
            key = k
    return key, value


my_dict = count_words('This is a sample sample sample words, this')
print(most_common(my_dict))
