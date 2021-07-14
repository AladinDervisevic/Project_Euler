# A googol (10 ** 100) is a massive number: one followed by one-hundred zeros;
# 100 ** 100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, a ** b, where a, b < 100, 
# what is the maximum digital sum?
#_____________________________________________________________________________

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

max_digital_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        digital_sum = sum_of_digits(a ** b)
        if digital_sum >= max_digital_sum:
            max_digital_sum = digital_sum
print(max_digital_sum)