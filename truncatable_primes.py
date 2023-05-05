# The number 3797 has an interesting property. 
# Being prime itself, it is possible to continuously 
# remove digits from left to right, and remain prime at each stage: 
# 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are 
# both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
#__________________________________________________________________

from time import time

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

def from_left(number):
    while number > 9:
        number = int(str(number)[1:])
        if not is_prime(number):
            return False
    return True

def from_right(number):
    while number > 9:
        number //= 10
        if not is_prime(number):
            return False
    return True

def truncatable_primes():
    primes = get_primes(10 ** 6)
    truncatable = set()
    for p in primes:
        if p < 10:
            continue
        if from_left(p) and from_right(p):
            truncatable.add(p)
        if len(truncatable) == 11:
            return sum(truncatable) 
        
def main():
    start = time()
    resitev = truncatable_primes()
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()