# The number, 1406357289, is a 0 to 9 pandigital number because 
# it is made up of each of the digits 0 to 9 in some order, 
# but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. 
# In this way, we note the following:
# d2 * d3 * d4 = 406 is divisible by 2
# d3 * d4 * d5 = 063 is divisible by 3
# d4 * d5 * d6 = 635 is divisible by 5
# d5 * d6 * d7 = 357 is divisible by 7
# d6 * d7 * d8 = 572 is divisible by 11
# d7 * d8 * d9 = 728 is divisible by 13
# d8 * d9 * d10 =289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
#__________________________________________________________________

from time import time
from itertools import permutations

def property_check(num):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        if int(num[i + 1 : i + 4]) % divisors[i] != 0:
            return False
    return True

def digit_product(n):
    if n < 10:
        return n
    return n % 10 * digit_product(n // 10)

def main():
    start = time()

    resitev = 0
    for perm in permutations('0123456789'):
        if perm[0] != '0':
            number = ''.join(perm)
            if property_check(number):
                resitev += int(number)

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()