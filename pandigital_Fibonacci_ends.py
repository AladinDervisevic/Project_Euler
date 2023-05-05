# The Fibonacci sequence is defined by the recurrence relation:
# F_n = F_(n−1) + F_(n−2), where F_1 = 1 and F_2 = 1.
# It turns out that F_541, which contains 113 digits, is the first 
# Fibonacci number for which the last nine digits are 1-9 pandigital 
# (contain all the digits 1 to 9, but not necessarily in order).
# And F_2749, which contains 575 digits, is the first Fibonacci number 
# for which the first nine digits 
# are 1-9 pandigital.
# Given that F_k is the first Fibonacci number for which the 
# first nine digits AND the last nine digits are 1-9 pandigital, find k.
#_______________________________________________________________________

# https://en.wikipedia.org/wiki/Fibonacci_number

from time import time
from math import log10

def is_pandigital(number):
    return all(i in str(number) for i in '123456789')

def pandigital_fibonacci_ends():
    k = 2
    a, b = 1, 1
    phi = (1 + 5 ** 0.5) / 2
    while True:
        a, b = b, (a + b) % 10 ** 9
        k += 1
        if is_pandigital(b): # checks last 9 digits
            num = k * log10(phi) + log10(1 / (5 ** 0.5))
            first = int(pow(10, num - int(num) + 8))
            if is_pandigital(first):
                return k

def main():
    start = time()
    resitev = pandigital_fibonacci_ends()
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()