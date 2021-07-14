# The number, 197, is called a circular prime 
# because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
#______________________________________________________

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def rotations_of_prime(n):
    ln = len(str(n))
    rotations = [n]
    while ln > 1:
        n = int(str(n)[1:] + str(n)[0])
        rotations.append(n)
        ln -= 1
    return rotations

def circular_primes(n):
    rot_primes = 0
    primes = get_primes(n)
    for prime in primes:
        if ((prime < 10 or not any(c in '024568' for c in str(prime))) and 
        all(rotation in primes for rotation in rotations_of_prime(prime))):
            rot_primes += 1
    return rot_primes

print(circular_primes(10 ** 6))