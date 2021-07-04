def prime_factors(num):
    '''This function takes a number "num" and returns its prime factors'''
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    i = 0
    divisors = []
    while num != 1:
        # if a is divisible by a prime
        if num % primes[i] == 0:
            num //= primes[i]
            divisors.append(primes[i])
        else:
            i += 1
    return divisors


print(prime_factors(13))
