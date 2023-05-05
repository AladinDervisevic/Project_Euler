# 2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2 ** 1000?
#_______________________________________________________

from time import time

def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def main():
    start = time()
    resitev = digit_sum(2 ** 1000)
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()