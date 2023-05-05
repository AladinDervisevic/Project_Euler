# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have 
# three distinct prime factors are:
# 644 = 2 ** 2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have 
# four distinct prime factors each.
# What is the first of these numbers?
#___________________________________________________________________________

import time

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

def prime_factors(n, distinct_primes, divisor = 2):
    if is_prime(n):
        return [n]
    
    if n in distinct_primes:
        return distinct_primes[n]
    
    for i in range(divisor, n + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            divisor = i
            break
    return [divisor] + prime_factors(n, distinct_primes, divisor + 1)

def main():
    start = time.time()

    distinct_primes = {1: [], 2: [2], 3: [3]}  # number : list of distinct prime factors
    first, second, third, fourth = 1, 2, 3, 4

    while True:
        distinct_primes[fourth] = prime_factors(fourth, distinct_primes)
        if all(4 == len(distinct_primes[i]) for i in [first, second, third, fourth]):
            resitev = first
            break
        first, second, third, fourth = second, third, fourth, fourth + 1

    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()