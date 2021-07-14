# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, binom_(3)^(5) = 10
# In general, binom_(r)^(n) = (n!) // (r! * (n-r)!), where r <= n 
# It is not until n=23, that a value exceeds one-million: 
# binom_(10)^(23) = 1144066
# How many, not necessarily distinct, values of binom_(r)^(n) 
# for 1 <= n <= 100, are greater than one-million?
#________________________________________________________________

def factorial(n, start = 1):
    if n == 0:
        return 1
    if start == n:
        return start
    else:
        middle = (n + start) // 2
        return factorial(middle, start) * factorial(n, middle + 1)

def binom(n, r):
    if r > n:
        return 'error : r > n'
    if r == 0:
        return 1
    else:
        return factorial(n) // (factorial(r) * factorial(n - r))

counter = 0
for n in range(1, 101):
    for r in range(1, 101):
        if r <= n and binom(n, r) > 1000000:
            counter += 1
print(counter)