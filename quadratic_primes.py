# Euler discovered the remarkable quadratic formula: n ** 2 + n + 41
# It turns out that the formula will produce 40 primes 
# for the consecutive integer values 0 ≤ n ≤ 39.
# However, when n = 40, 40 ** 2 + 40 + 41 = 40 * (40 + 1) + 41 
# is divisible by 41, and certainly when n = 41, 41 ** 2 + 41 + 41 
# is clearly divisible by 41.
# The incredible formula n ** 2 − 79 * n + 1601 was discovered, 
# which produces 80 primes for the consecutive values 0≤n≤79. 
# The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form: n ** 2 + a * n + b, 
# where |a| < 1000 and |b| ≤ 1000, 
# where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |−4| = 4. 
# Find the product of the coefficients, a and b, 
# for the quadratic expression that produces the 
# maximum number of primes for consecutive values of n, starting with n = 0.
#___________________________________________________________________________

from time import time

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

def number_of_consecutive_primes(a, b):
    counter, n = 0, 0
    while True:
        number = n ** 2 + a * n + b
        if is_prime(number):
            counter += 1
            n += 1
        else:
            return counter

def main():
    start = time()

    coefficients = {}
    for a in range(-999, 1000, 2): # skipping even numbers because the formula would be divisible by 2
        for b in range(-999, 1001, 2): 
            sequence_length = number_of_consecutive_primes(a, b)
            if sequence_length > 0:
                coefficients[(a, b)] = sequence_length
    wanted_pair = max((v, k) for k, v in coefficients.items())
    resitev = wanted_pair[1][0] * wanted_pair[1][1]
    
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()