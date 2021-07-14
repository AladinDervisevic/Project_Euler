# The infinite continued fraction can be written, sqrt(2) = [1;(2)], (2) 
# indicates that 2 repeats ad infinitum.
# In a similar way, sqrt(23) = [4;(1,3,1,8)].
# What is most surprising is that the important mathematical constant,
# e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].
# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536,...
# The sum of digits in the numerator of the 10th convergent is 
# 1 + 4 + 5 + 7 = 17
# Find the sum of digits in the numerator of the 100th convergent 
# of the continued fraction for e.
#________________________________________________________________________

def digit_sum(number):
    if number < 10:
        return number
    return number % 10 + digit_sum(number // 10)

def convergents_of_e():
    e, k = [], 0
    for i in range(1, 100):
        if i % 3 == 2:
            k += 1
            e.append(2 * k)
        else:
            e.append(1)
    from math import gcd
    numerator = 1
    denominator = e[-1]
    for i in list(reversed(e))[1:]:
        numerator = numerator + i * denominator
        numerator, denominator = denominator, numerator
    numerator = numerator + denominator * 2
    numerator //= gcd(numerator, denominator)
    return digit_sum(numerator)

print(convergents_of_e())