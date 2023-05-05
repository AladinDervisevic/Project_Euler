# The sum of the squares of the first ten natural numbers is,
# 1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers
# and the square of the sum is:
# 3025 − 385 = 2640
# 3025 − 385 = 2640
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers
# and the square of the sum.
#__________________________________________________________________

from time import time

def main():
    start = time()
    difference = sum(range(101)) ** 2 - sum(i ** 2 for i in range(101))
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {difference}\nporabljen cas = {cas}")

main()