# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
divisor = 2
prime_factors = []
while number != 1:
    if number % divisor == 0:
        prime_factors.append(divisor)
        while number % divisor == 0:
            number //= divisor
    divisor += 1
print(max(prime_factors))