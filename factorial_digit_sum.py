# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is:
# 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
#_______________________________________________________
from math import factorial
import time

def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def main():
    start = time.time()

    resitev = digit_sum(factorial(100))

    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()