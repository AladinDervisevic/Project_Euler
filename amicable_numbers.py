# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
# and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are: 
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110, 
# therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
#__________________________________________________________________________

from time import time

def divsum(N):
    div_sum = [1] * N
    for i in range(2, int(N ** 0.5)):
        for j in range(i + 1, N // i):
            div_sum[i * j] += i + j
    return div_sum

def amicable_numbers_under(n):
    amicable_numbers = []
    d = divsum(n * 10)
    for a in range(1, n): # O(n)
        if a in amicable_numbers:
            continue
        b = d[a] 
        if d[b] == a and a != b:
            amicable_numbers.append(a)
            amicable_numbers.append(b)
    print(f"{amicable_numbers}")
    return sum(amicable_numbers)

def main():
    start = time()
    resitev = amicable_numbers_under(10 ** 4)
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()