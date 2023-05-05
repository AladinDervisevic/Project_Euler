# A googol (10 ** 100) is a massive number: one followed by one-hundred zeros;
# 100 ** 100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, a ** b, where a, b < 100, 
# what is the maximum digital sum?
#_____________________________________________________________________________

from time import time

def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def main():
    start = time()

    max_digital_sum = 0
    for a in range(100):
        for b in range(100):
            digital_sum = digit_sum(a ** b)
            if digital_sum >= max_digital_sum:
                max_digital_sum = digital_sum

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {max_digital_sum}\nporabljen cas = {cas}")

main()