# It can be seen that the number, 125874, and its double, 251748, 
# contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
# contain the same digits.
#_________________________________________________________________________
from time import time
from itertools import permutations

def main():
    start = time()

    n = 125874
    resitev = 0
    while not resitev:
        l = len(str(n))
        if l < len(str(6 * n)):
            n = 10 ** l
        perms = set(
            int(''.join(i)) for i in permutations(str(n)) if i[0] != '0'
        )
        for x in perms:
            if all(j * x in perms for j in range(2, 7)):
                resitev = x
        n += 1

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()