# Euler's Totient function, φ(n) [sometimes called the phi function], 
# is used to determine the number of numbers less than n which are 
# relatively prime to n. 
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine 
# and relatively prime to nine, φ(9)=6.
# n	 | Relatively Prime	| φ(n)  | n/φ(n)
# 2	 | 1	            |  1    | 2
# 3	 | 1,2	            |  2    | 1.5
# 4	 | 1,3	            |  2    | 2
# 5	 | 1,2,3,4	        |  4    | 1.25
# 6	 | 1,5	            |  2    | 3
# 7	 | 1,2,3,4,5,6      |  6    | 1.1666...
# 8	 | 1,3,5,7	        |  4    | 2
# 9	 | 1,2,4,5,7,8      |  6    | 1.5
# 10 | 1,3,7,9	        |  4    | 2.5
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
#_______________________________________________________________

# source : https://en.wikipedia.org/wiki/Euler%27s_totient_function 

# Euler's product formula : 
# phi(n) = n * (1 - 1 / p)  for p in prime factors of n
# From that we see the wanted ratio as : 
# n / phi(n) = p / (p - 1) for p in prime factors of n

from time import time

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def main():
    start = time()

    n = 1
    for prime in get_primes(10 ** 3):
        if n * prime > 10 ** 6:
            break
        n *= prime

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {n}\nporabljen cas = {cas}")

main()