# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#______________________________________________________________

import time

def largest_prime_factor(number):
    prime = 2
    while True:
        if number % prime == 0:
            while number % prime == 0:
                number //= prime
            if number == 1:
                break
        if prime == 2:
            prime += 1
        else:
            prime += 2
    return prime

def main():
    start = time.time()
    number = 600851475143
    resitev = largest_prime_factor(number)
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()