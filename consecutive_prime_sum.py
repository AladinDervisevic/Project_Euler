# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
#__________________________________________________________________________________________

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

def next_prime(number):
    x = number + 1
    while not is_prime(x):
        x += 1
    return x

answer = 0
sequence_length = 0
for start in range(2, 10 ** 3):
    if is_prime(start):
        local_sum, last_prime = start, start
        counter = 1
        while local_sum < 10 ** 6:
            if is_prime(local_sum) and counter >= sequence_length:
                sequence_length = counter
                answer = local_sum
            local_sum += next_prime(last_prime)
            last_prime = next_prime(last_prime)
            counter += 1
print(answer)