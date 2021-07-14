# A positive fraction whose numerator is less than its denominator 
# is called a proper fraction.
# For any denominator, d, there will be d−1 proper fractions; 
# for example, with d = 12:
# 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), 
# to be the ratio of its proper fractions that are resilient; 
# for example, R(12) = 4/11
# In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10
# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
#_____________________________________________________________________________

# I used Euler's totient function : 
# fi(n) = n * PI_(p|n) (1 - 1/p) = n * (1 - 1/p_1) *...* (1 - 1/p_m), 
# where p_1, ... , p_m are prime factors of n
# source : https://en.wikipedia.org/wiki/Euler%27s_totient_function
# source : https://mathworld.wolfram.com/TotientFunction.html

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

def get_prime_factors(number):
    factors = set()
    while number > 1:
        for num in range(2, number + 1):
            if number % num == 0 and is_prime(num):
                factors.add(num)
                number //= num
            if number == 1:
                break
    return factors

# returns the number of resilient fractions with the given denominator 
def resilient(denominator):
    prime_factors = get_prime_factors(denominator)
    resilient_fractions = denominator
    for prime in prime_factors:
        resilient_fractions *= (1 - 1 / prime)
    return resilient_fractions

def next_prime(prime):
    x = prime + 2
    while True:
        if is_prime(x):
            return x
        x += 2

def next_composite_number(number):
    x = number + 1
    while True:
        if not is_prime(x):
            return x
        x += 1

def resilience():
    goal_ratio = 15499 / 94744
    ratio = 1
    denominator = 6      #  2 * 3
    last_prime = 3
    while ratio >= goal_ratio: # at the end I'll have a product of sequental primes for which R(product) exceeds the ratio
        denominator *= next_prime(last_prime)
        last_prime = next_prime(last_prime)
        ratio = resilient(denominator) / (denominator - 1)
    denominator //= last_prime  # I back down one prime and now R(product) does not exceed the ratio
    ratio = 1
    last_composite = 1
    while ratio >= goal_ratio:  # I multiply by composite numbers until I get the wanted ratio
        denominator *= next_composite_number(last_composite)
        last_composite = next_composite_number(last_composite)
        ratio = resilient(denominator) / (denominator - 1)
    return denominator

print(resilience())

# Runtime : 1min 8s