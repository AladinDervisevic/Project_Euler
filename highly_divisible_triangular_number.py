# The sequence of triangle numbers is generated 
# by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the divisors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number 
# to have over five hundred divisors?
#____________________________________________________________________________

import time

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

# function that checks how many divisors a number has
def number_of_divisors(number):
    if is_prime(number):
        return 2
    limit = int(number ** 0.5)
    counter = 0
    for i in range(1, limit + 1):
        if number % i == 0:
            counter += 1
    return counter * 2
    # 1 to the square root of the number holds exactly half of the divisors

def hig_div_tri_num():
    triangle_number, index = 1, 1
    while number_of_divisors(triangle_number) <= 500:
        index += 1
        triangle_number += index
    return triangle_number

def main():
    start = time.time()
    resitev = hig_div_tri_num()
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()