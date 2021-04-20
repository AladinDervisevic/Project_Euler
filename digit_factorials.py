# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums, they are not included.
#________________________________________________________________________________________
import math

def sum_of_digit_factorials(n):
    return sum(math.factorial(int(i)) for i in str(n))

result = sum(i for i in range(10, 10 ** 5) if sum_of_digit_factorials(i) == i)
print(result)