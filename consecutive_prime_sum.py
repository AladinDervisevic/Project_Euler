# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that 
# adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that 
# adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, 
# can be written as the sum of the most consecutive primes?
#___________________________________________________________________

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

def next_prime(n):
    if n == 2:
        return 3
    x = n + 2
    while not is_prime(x):
        x += 2
    return x

def main():
    start_time = time.time()
    answer = 0
    max_length = 0
    for start in range(2, 10 ** 3):
        if is_prime(start):
            local_sum, last_prime = start, start
            counter = 1
            while local_sum < 10 ** 6:
                if is_prime(local_sum) and counter >= max_length:
                    max_length = counter
                    answer = local_sum
                last_prime = next_prime(last_prime)
                local_sum += last_prime
                counter += 1
    end = time.time()
    cas = round(end - start_time, 2)
    print(f"resitev = {answer}\nporabljen cas = {cas}")

main()