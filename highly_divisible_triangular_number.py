# The sequence of triangle numbers is generated 
# by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number 
# to have over five hundred divisors?
#____________________________________________________________________________

# function that checks how many divisors a number has
def number_of_divisors(number):
    limit = int(number ** 0.5)
    counter = 0
    for i in range(1, limit + 1):
        if number % i == 0:
            counter += 1
    return counter * 2
    # 1 to the square root of the number holds exactly half of the divisors

def hig_div_tri_num():
    triangle_number, place_of_number = 1, 1
    while number_of_divisors(triangle_number) <= 500:
        place_of_number += 1
        triangle_number += place_of_number
    return triangle_number

print(hig_div_tri_num())