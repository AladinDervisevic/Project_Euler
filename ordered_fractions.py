# Consider the fraction, n/d, where n and d are positive integers.
# If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 
# in ascending order of size, we get:
# 
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
# 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
# By listing the set of reduced proper fractions for d ≤ 1,000,000 
# in ascending order of size, 
# find the numerator of the fraction immediately to the left of 3/7.
#________________________________________________________________________

import time
from math import gcd

def main():
    start = time.time()

    denominator = 0
    for d in range(10 ** 6, 1, -1):
        if d % 7 == 0:
            denominator = d
            break
    numerator = 3 * (denominator // 7)
    while gcd(numerator, denominator) != 1:
        numerator -= 1
    
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {numerator}\nporabljen cas = {cas}")

main()