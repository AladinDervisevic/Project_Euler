# A unit fraction contains 1 in the numerator. 
# The decimal representation of the unit fractions with 
# denominators 2 to 10 are given:
# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
# It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains 
# the longest recurring cycle in its decimal fraction part.
#___________________________________________________________________

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
    
def recyprocal_primes():
    for denominator in range(999, 6, -1):
        if is_prime(denominator):
            period = 1
            while pow(10, period, denominator) != 1:  # <=> (10 ** period) % denominator (Fermat's little theorem)
                period += 1
            if denominator - 1 == period: # checking if the denominator is a full reptend prime
                return denominator

def main():
    start = time()
    resitev = recyprocal_primes()
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()