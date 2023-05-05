# We shall say that an n-digit number is pandigital if it makes use 
# of all the digits 1 to n exactly once.
# For example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way 
# so be sure to only include it once in your sum.
#_____________________________________________________________________________
from time import time
from itertools import permutations

def main():
    start = time()

    sum = 0
    identity = {}
    perms = [''.join(i) for i in permutations('123456789')]
    for i in range(1, 4):
        j = i + 3
        if i == 1:
            j = 5
        for perm in perms:
            multiplicand = int(perm[:i])
            multiplier = int(perm[i:j])
            product = int(perm[j:])
            if multiplicand * multiplier == product:
                if product not in identity:
                    sum += product
                identity[product] = [multiplicand, multiplier]
    print(identity)
    
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {sum}\nporabljen cas = {cas}")

main()