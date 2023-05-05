# Euler's Totient function, φ(n) [sometimes called the phi function],
# is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. 
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
# Find the value of n, 1 < n < 10 ** 7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
#_______________________________________________________________________________________________________________

# https://en.wikipedia.org/wiki/Euler%27s_totient_function

# ratio n/φ(n) smallest <=> φ(n) very big <=> n is a product of primes of order 1

from time import time

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def factorize(n, primes=None):
    if primes is None:
        primes = get_primes(int(n ** 0.5))
    factors = {}
    for p in primes:
        if p ** 2 > n:
            break
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k > 0:
            factors[p] = k
    if n > 1:
        factors[n] = 1
    return factors

def phi(n):
    product = n
    for p in factorize(n):
        product *= (p - 1)
        product //= p
    return product

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b)) 

def main():
    start = time()
    
    min = 2 / 1
    resitev = 2
    primes = sorted(set(get_primes(5 * 10 ** 3)) - set(get_primes(10 ** 3)))
    l = len(primes)
    for i in primes[l // 3: ]:
        for j in primes[l // 3: ]:
            n = i * j
            if n >= 10 ** 7 or i < j:
                break
            phi_n = phi(n)
            if not is_permutation(n, phi_n):
                continue
            ratio = n / phi_n
            if ratio < min:
                min = ratio
                resitev = n

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()

# 8319823
# 10s