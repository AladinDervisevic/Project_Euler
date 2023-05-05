# A Pythagorean triplet is a set of three natural numbers, 
# a < b < c, for which, a ** 2 + b ** 2 = c ** 2
# For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a * b * c.
#_________________________________________________________________________

from math import sqrt
from time import time

def pythagorean_triplets():
    product = 0
    for a in range(1,300):
        for b in range(1,400):
            if a < b:
                c = sqrt(a ** 2 + b ** 2)
                if a + b + c == 1000:
                    product = int(a * b * c)
                    return product

def main():
    start = time()
    resitev = pythagorean_triplets()
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()