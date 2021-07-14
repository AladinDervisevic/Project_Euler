# Comparing two numbers written in index form like 2 ** 11 and 3 ** 7 
# is not difficult, as any calculator would confirm that 
# 2 ** 11 = 2048 < 3 ** 7 = 2187.
# However, confirming that 632382 ** 518061 > 519432 ** 525806 would be 
# much more difficult, as both numbers contain over three million digits.
# Using base_exp.txt, a 22K text file containing one thousand lines 
# with a base/exponent pair on each line, determine which line number 
# has the greatest numerical value.
# NOTE: The first two lines in the file represent the numbers 
# in the example given above.
#________________________________________________________________________
import os
os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

with open('base_exp.txt', encoding = 'utf-8') as dat:
    numbers = []
    for string_pair in dat.read().split('\n'):
        pair = tuple([int(i) for i in string_pair.split(',')])
        numbers.append(pair)
    from math import log
    candidates = []
    for base, exp in numbers:
        candidates.append(exp * log(base))
    index = candidates.index(max(candidates))
    print(index + 1)