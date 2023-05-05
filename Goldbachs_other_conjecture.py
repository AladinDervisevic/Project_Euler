# It was proposed by Christian Goldbach that every odd composite number 
# can be written as the sum of a prime and twice a square.
# 9 = 7 + 2× 1 ** 2
# 15 = 7 + 2 × 2 ** 2
# 21 = 3 + 2 × 3 ** 2
# 25 = 7 + 2 × 3 ** 2
# 27 = 19 + 2 × 2 ** 2
# 33 = 31 + 2 × 1 ** 2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written 
# as the sum of a prime and twice a square?
#________________________________________________________________________

import time
from math import sqrt

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def is_prime(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True

def test(number):
    primes = get_primes(number)
    for prime in primes[::-1]:
        for i in range(1, int(sqrt(number // 2)) + 1):
            if number == prime + 2 * i ** 2:
                return True
    return False

def main():
    start = time.time()

    resitev = 1
    while True:
        resitev += 2
        if is_prime(resitev):
            continue
        if not test(resitev):
            break

    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()