# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
#________________________________________________________________

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

def nth_prime(n):
    number, counter = 3, 1
    while True:
        if is_prime(number):
            counter += 1
            if counter == n:
                return number
        number += 2

def main():
    start = time.time()
    resitev = nth_prime(10001)
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()