# The number 512 is interesting because it is equal to the sum of 
# its digits raised to some power:
# 5 + 1 + 2 = 8, and 8 ** 3 = 512. 
# Another example of a number with this property is 614656 = 28 ** 4.
# We shall define an to be the nth term of this sequence and insist 
# that a number must contain
# at least two digits to have a sum.
# You are given that a_2 = 512 and a_10 = 614656.
# Find a_30.
#_____________________________________________________________________
import time

def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

def digit_power_sum():
    powers = []
    for i in range(2, 100):
        for j in range(2, 100):
            power = pow(i, j)
            if digit_sum(power) == i:
                powers.append(power)
    return sorted(powers)[29]

def main():
    start = time.time()
    resitev = digit_power_sum()
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()