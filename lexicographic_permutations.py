# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits:
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#___________________________________________________________________________

from time import time
from itertools import permutations

def main():
    start = time()
    perms = list(permutations(list('0123456789')))
    resitev = "".join(perms[10 ** 6 - 1])
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()