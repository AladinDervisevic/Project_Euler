# Starting in the top left corner of a 2×2 grid, 
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
#______________________________________________________

from time import time
from math import factorial

def main():
    start = time()
    n = 20
    resitev = factorial(2 * n) // (factorial(n) ** 2)
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()