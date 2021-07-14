# The primes 3, 7, 109, and 673, are quite remarkable. 
# By taking any two primes and concatenating them in any order 
# the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime. 
# The sum of these four primes, 792, represents the lowest sum 
# for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes 
# concatenate to produce another prime.
#______________________________________________________________________
from itertools import permutations

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

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def all_combos_are_prime(primes):
    perms = list(permutations(primes, 2))
    return all(is_prime(int(str(pair[0]) + str(pair[1]))) for pair in perms)

def possible_solution(list_of_primes):
    if len(list_of_primes) == 5:
        return list_of_primes
    primes = get_primes(10 ** 4)
    for prime in primes:
        if (prime > list_of_primes[-1] and 
        all_combos_are_prime(list_of_primes + [prime])):
            check = possible_solution(list_of_primes + [prime])
            if check:
                return check
    return False

solution = 0
primes = get_primes(10 ** 4)
while not solution:
    solution = possible_solution([primes.pop(0)])
print(sum(solution))

# Runtime : 2min