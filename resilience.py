# A positive fraction whose numerator is less than its denominator 
# is called a proper fraction.
# For any denominator, d, there will be d−1 proper fractions; 
# for example, with d = 12:
# 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), 
# to be the ratio of its proper fractions that are resilient; 
# for example, R(12) = 4/11
# In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10
# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
#_____________________________________________________________________________

# Euler's totient function : 
# fi(n) = n * PI_(p|n) (1 - 1/p) = n * (1 - 1/p_1) *...* (1 - 1/p_m), 
# where p_1, ... , p_m are prime factors of n
# source : https://en.wikipedia.org/wiki/Euler%27s_totient_function
# source : https://mathworld.wolfram.com/TotientFunction.html

from time import time
    
def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

# returns the number of resilient fractions with the given denominator 
def R(d, primes):
    prime_factors = set()
    for i in primes:
        if d % i == 0:
            prime_factors.add(i)
        if i > d:
            break        
    totient = d
    for p in prime_factors:
        totient *= (1 - 1 / p)
    return totient / (d - 1)

def main():
    start = time()

    primes = get_primes(10 ** 6)
    GOAL_RATIO = 15499 / 94744
    d = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23
    resitev = d
    while R(resitev, primes) >= GOAL_RATIO:
        resitev += d

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()