# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#__________________________________________________________________________________________________________

def smallest_num_div_by_1_to_20():
    start = 2 * 7 * 11 * 13 * 17 * 18 * 19 * 20
    for i in range(start, 10 ** 10):
        if all(i % j == 0 for j in range(1, 21)):
            return i

print(smallest_num_div_by_1_to_20())