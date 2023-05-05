# The number, 197, is called a circular prime 
# because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
#______________________________________________________

from time import time

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def rotations_of(n):
    L = len(str(n))
    rotations = [n]
    while L > 1:
        n = int(str(n)[1:] + str(n)[0])
        rotations.append(n)
        L -= 1
    return rotations

def circular_primes(n):
    rot_primes = 0
    primes = set(get_primes(n))
    for prime in primes:
        if ((prime < 10 or not any(c in '024568' for c in str(prime))) and
        all(i in primes for i in rotations_of(prime))):
            rot_primes += 1
    return rot_primes

def main():
    start = time()
    resitev = circular_primes(10 ** 6)
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()