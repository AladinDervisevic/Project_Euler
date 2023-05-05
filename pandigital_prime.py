# We shall say that an n-digit number is pandigital if it makes use of 
# all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
#____________________________________________________________________

from time import time
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
        
def main():
    start = time()

    pandigitals = []
    resitev = 0
    for i in range(4, 8):
        for j in [int(''.join(p)) for p in permutations('1234567', i)]:
            pandigitals.append(j) 
    for i in sorted(pandigitals, reverse = True):
        if is_prime(i):
            resitev = i
            break

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()