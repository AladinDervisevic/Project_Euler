# It is possible to show that the square root of two can be expressed 
# as an infinite continued fraction.
# sqrt(2) = 1 + ( 1 / (2 + 1 / (2 + 1/ (2 + ...))) )
# By expanding this for the first four iterations, we get:
# 1 + 1 / 2 = 3 / 2 = 1.5
# 1 + 1 / (2 + 1 / 2) = 7 / 5 = 1.4
# 1 + 1 / (2 + 1 / (2 + 1 / 2)) = 17 / 12 = 1.41666...
# 1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / 2))) = 41 / 29 = 1.41379...
# The next three expansions are 99 / 70 , 239 / 169 , 577 / 408 , 
# but the 8th expansion, 1393 / 985, is
# the first example where the number of digits in the numerator 
# exceeds the number of digits in the denominator.
# In the first one-thousand expansions, how many fractions contain 
# a numerator with more digits than the denominator?
#______________________________________________________________________

# What I found out: 
# Let n be the number of steps we took to expand the fraction.
# numerator_n = numerator_(n-1) + 2 * denominator_(n-1)
# denominator_n = numerator_(n-1) + denominator_(n-1)

numerator, denominator, counter = 1, 1, 0
for _ in range(1000): # 1k expansions
    numerator, denominator = numerator + 2 * denominator, numerator + denominator
    if len(str(numerator)) > len(str(denominator)):
        counter += 1
print(counter)