# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
#___________________________________________________________________________________
import itertools

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

primes = sorted(set(get_primes(10000)) - set(get_primes(1000)))
perms = []
perm_list = []
answer = set()
for prime in primes:
    perm_list = list(itertools.permutations(list(str(prime))))
    perms = sorted(int(''.join(list(perm))) for perm in perm_list if perm[0] != '0')
    for i in perms:
        for j in perms:
            for z in perms:
                if j - i == z - j and i < j < z and all(k in primes for k in [i, j, z]):
                    answer.add((i, j, z))
answer = list(answer - {(1487, 4817, 8147)})[0] # this is a tuple now
result = ''
for number in answer:
    result += str(number)
print(result)
    
