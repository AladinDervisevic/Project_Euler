# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
# and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are: 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, 
# therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
#__________________________________________________________________________

import time

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def prastevilski_razcep(n):
    if n == 1:
        return [(1, 1)]
    razcep = []
    prastevila = get_primes(n)
    prastevila.append(n)
    while n > 1:
        exp = 0
        p = prastevila.pop(0)
        while n % p != 0:
            p = prastevila.pop(0)
        while n % p == 0:
            n //= p
            exp += 1
        if exp > 0:
            razcep.append((p, exp))
    return razcep

# https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Elementary_Number_Theory_(Raji)/04%3A_Multiplicative_Number_Theoretic_Functions/4.02%3A_Multiplicative_Number_Theoretic_Functions

def d(n):
    if n < 10:
        return n
    razcep = prastevilski_razcep(n)
    D = 1
    while razcep:
        p, exp = razcep[0]
        D *= ( (p ** (exp + 1) - 1) // (p - 1))
        razcep = razcep[1:]
    return D - n

def amicable_numbers_under(n):
    amicable_numbers = []
    for a in range(1, n): # O(n)
        if a in amicable_numbers:
            continue
        b = d(a) 
        if d(b) == a and a != b:
            amicable_numbers.append(a)
            amicable_numbers.append(b)
    print(f"{amicable_numbers}")
    return sum(amicable_numbers)

def main():
    start = time.time()
    resitev = amicable_numbers_under(10 ** 4)
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()