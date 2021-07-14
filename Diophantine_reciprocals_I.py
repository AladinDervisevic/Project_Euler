# In the following equation x, y, and n are positive integers.
# 1 / x + 1 / y = 1 / n
# For n = 4 there are exactly three distinct solutions:
# 1 / 5 + 1 / 20  = 1 / 4
# 1 / 6 + 1 / 12 = 1 / 4
# 1 / 8 + 1 / 8 = 1 / 4
# What is the least value of n for which the number of distinct solutions 
# exceeds one-thousand?
#________________________________________________________________________
# if x = n + a and y = n + b --> n ** 2 = a * b

def get_divisors(number): 
    limit = int(number ** 0.5)
    counter = 0
    for i in range(1, limit + 1):
        if number % i == 0:
            counter += 1
    return counter * 2 

n = 2 * 3 * 5 * 7 * 11 * 13 * 2 * 3
while True:
    if (get_divisors(n ** 2) + 1) // 2 > 1000:
        print(n)
        break
    n += 1