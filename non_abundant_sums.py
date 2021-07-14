# A perfect number is a number for which the sum of its proper divisors 
# is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 
# 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors 
# is less than n and 
# it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers 
# is 24. 
# By mathematical analysis, it can be shown that all integers greater than 
# 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed 
# as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written 
# as the sum of two abundant numbers.
#_____________________________________________________________________________

def abundant(number):
    if is_prime(number):
        return False
    return sum([i for i in range(1, number) if number % i == 0]) > number

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

abundant_numbers = [number for number in range(1, 28124) if abundant(number)]
sum_of_two_abundant_numbers = set()
for i in abundant_numbers:
    index = abundant_numbers.index(i)
    for j in abundant_numbers[index:]:
        sum_of_two_abundant_numbers.add(i + j)
result = sum(set(range(1,28124)) - sum_of_two_abundant_numbers)
print(result)

# RunTime : 30s