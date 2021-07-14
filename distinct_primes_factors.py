# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have 
# three distinct prime factors are:
# 644 = 2 ** 2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have 
# four distinct prime factors each.
# What is the first of these numbers?
#___________________________________________________________________________

def distinct_prime_factors(n, values, divisor = 2):
    if n in values:
        return values[n]
    for i in range(divisor, n + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            divisor = i
            break
    return [divisor] + distinct_prime_factors(n, values, divisor + 1)

values = {1: [], 2: [2], 3: [3], 4: [2]}  # number : list of distinct prime factors
first, second, third, fourth = 2, 3, 4, 5
while True:
    values[fourth] = distinct_prime_factors(fourth, values)
    if all(4 == len(values[i]) for i in [first, second, third, fourth]):
        print(first)
        break
    first, second, third, fourth = second, third, fourth, fourth + 1

# RunTime ~ 56s