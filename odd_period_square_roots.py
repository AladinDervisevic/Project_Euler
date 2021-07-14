# All square roots are periodic when written as continued fractions and 
# can be written in the form:
# sqrt(N) = a_0 + 1 / (a_1 + (1 / a_2 + (1 / ...)))
# For example, let us consider sqrt(23):
# sqrt(23) = 4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / (...))))
# The process can be summarised as follows:
#
#   a_0 = 4, 1 / √(23) − 4 = (√(23) + 4) / 7   = 1 + (√(23) − 3) / 7 
#   a_1 = 1, 7 / √(23) − 3 = 7(√(23) + 3) / 14 = 3 + (√(23) − 3) / 2
#   a_2 = 3, 2 / √(23) − 3 = 2(√(23) + 3) / 14 = 1 + (√(23) − 4) / 7
#   a_3 = 1, 7 / √(23) − 4 = 7(√(23) + 4) / 7  = 8 + √(23) − 4
#   a_4 = 8, 1 / √(23) − 4 = (√(23) + 4) / 7   = 1 + (√(23) − 3) / 7
#   a_5 = 1, 7 / √(23) − 3 = 7(√(23) + 3) / 14 = 3 + (√(23) − 3) / 2
#   a_6 = 3, 2 / √(23) − 3 = 2(√(23) + 3) / 14 = 1 + (√(23) − 4) / 7
#   a_7 = 1, 7 / √(23) − 4 = 7(√(23) + 4) / 7  = 8 + √(23)−4
#
# It can be seen that the sequence is repeating. For conciseness, 
# we use the notation √(23) = [4;(1,3,1,8)], 
# to indicate that the block (1,3,1,8) repeats indefinitely.
# The first ten continued fraction representations of 
# (irrational) square roots are:
#
#   √2 = [1;(2)] , period = 1
#   √3 = [1;(1,2)], period = 2
#   √5 = [2;(4)], period = 1
#   √6 = [2;(2,4)], period = 2
#   √7 = [2;(1,1,1,4)], period = 4
#   √8 = [2;(1,4)], period = 2
#  √10 = [3;(6)], period = 1
#  √11 = [3;(3,6)], period = 2
#  √12 = [3;(2,6)], period = 2
#  √13 = [3;(1,1,1,1,6)], period = 5
#
# Exactly four continued fractions, for N≤13, have an odd period.
# How many continued fractions for N ≤ 10000 have an odd period?
#_______________________________________________________________________

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion 

counter = 0
candidates = sorted(set(range(2, 10 ** 4 + 1)) - set(i ** 2 for i in range(2, 101)))
for N in candidates:
    whole = int(N ** 0.5)
    r = whole
    k, period = 1, 0
    while k != 1 or period == 0:
        k = (N - r ** 2) // k
        r = (whole + r) // k * k - r
        period += 1
    if period % 2 != 0:
        counter += 1
print(counter)