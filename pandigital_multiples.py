# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying 
# by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
# which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed 
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?
#___________________________________________________________________________

from time import time
from itertools import permutations

def main():
    start = time()
    pandigitals = set(
        map(int, [''.join(i) for i in permutations('123456789')])
    )
    max_pan = 0
    for i in range(1, 10 ** 4):
        conc_product = f'{i}'
        n = 2
        while len(conc_product) < 9:
            conc_product += str(i * n)
            n += 1
        vrednost = int(conc_product)
        if vrednost in pandigitals and vrednost > max_pan:
            max_pan = vrednost
    resitev = max_pan
    
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()