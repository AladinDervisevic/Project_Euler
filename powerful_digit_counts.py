# The 5-digit number, 16807 = 7 ** 5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728 = 8 ** 9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?
#_______________________________________________________________________

# For calculating how many digits a number has we can use the formula: 
# int(log_10(n)) + 1
# n can't be greater than 10 since 10 ** n always has n + 1 digits

from math import log10

counter = 0
for n in range(1, 10):
    counter += int(1 / (1 - log10(n)))
print(counter)