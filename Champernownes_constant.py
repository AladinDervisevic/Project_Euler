# An irrational decimal fraction is created by concatenating 
# the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If d_n represents the n^th digit of the fractional part, 
# find the value of the following expression.
# d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
#________________________________________________________________

decimals, integer = '.', 1
while len(decimals) <= 10 ** 6:
    decimals += str(integer)
    integer += 1
result = 1
for i in range(1, 7):
    result *= int(decimals[10 ** i])
print(result)