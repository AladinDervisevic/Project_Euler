# PROBLEM 94

from time import time
from math import ceil, floor

def is_integer(x):
    return floor(x) == ceil(x)

def main():
    start = time()
    resitev = 0
    LIMIT1 = floor(((10 ** 9 - 1) / 3) ** 0.5)
    LIMIT2 = 31630
    
    for b in set(i ** 2 + 1 for i in range(1, LIMIT1)): # a = b + 1, where a is base, b is the lateral side
        area = ((3 * b + 1) * (b - 1)) ** 0.5 / 2
        if is_integer(area):
            resitev += 3 * b + 1
            
    for b in set((2 * i ** 2 + 1) // 3 for i in range(3, LIMIT2)): # a = b - 1
        area = ((3 * b - 1) * (b + 1)) ** 0.5 / 2
        if is_integer(area):
            resitev += 3 * b - 1
            
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()