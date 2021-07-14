# A number chain is created by continuously adding the square of the 
# digits in a number to form a new number until it has been seen before.
# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# Therefore any chain that arrives at 1 or 89 will become stuck 
# in an endless loop. 
# What is most amazing is that EVERY starting number will 
# eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?
#_____________________________________________________________________

def sum_of_digit_squares(number):
    sum = 0
    while number > 0:
        sum += (number % 10) ** 2
        number//= 10
    return sum

counter = 0
for i in range(1, 10 ** 7):
    next_number = sum_of_digit_squares(i)
    while next_number not in {1, 89}:
        next_number = sum_of_digit_squares(next_number)
    if next_number == 89:
        counter += 1
print(counter)

# Takes about 1min 8s to finish.