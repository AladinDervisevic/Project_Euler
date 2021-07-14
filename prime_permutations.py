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
import itertools

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def prime_permutations():
    primes = sorted(set(get_primes(10000)) - set(get_primes(1000)))
    for prime in primes:
        perm_list = list(itertools.permutations(list(str(prime))))
        perms = sorted(
            int(''.join(list(perm))) for perm in perm_list if perm[0] != '0'
        )
        for i in perms:
            index_i = perms.index(i)
            for j in perms[index_i:]:
                index_j = perms.index(j)
                for z in perms[index_j:]:
                    if (j - i == z - j and i < j < z and i != 1487 and
                        all(k in primes for k in [i, j, z])):
                        return str(i) + str(j) + str(z)

print(prime_permutations())