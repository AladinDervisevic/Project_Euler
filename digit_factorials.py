# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum 
# of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums, they are not included.
#________________________________________________________________
import time
from math import factorial

def sum_of_digit_factorials(n):
    if n < 10:
        return factorial(n)
    return factorial(n % 10) + sum_of_digit_factorials(n // 10)

def main():
    start = time.time()
    resitev = sum(
        i for i in range(10, 10 ** 5) if sum_of_digit_factorials(i) == i
    )
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()