# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
# increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of 
# three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating 
# the three terms in this sequence?
#______________________________________________________________________

from time import time
from itertools import permutations

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            num = (n - i * i - 1) // (2 * i) + 1
            sieve[i * i :: 2 * i] = [False] * num
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def prime_permutations():
    primes = set(get_primes(10000)) - set(get_primes(1000))
    for prime in primes:
        perms = sorted(
            int(''.join(i)) for i in permutations(str(prime)) if i[0] != '0'
        )
        for ind_i, i in enumerate(perms):
            for ind_j, j in enumerate(perms[ind_i:]):
                for z in perms[ind_j:]:
                    if (j - i == z - j and i < j < z and i != 1487 and
                        all(k in primes for k in [i, j, z])):
                        return i * 10 ** 8 + j * 10 ** 4 + z

def main():
    start = time()
    resitev = prime_permutations()
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()