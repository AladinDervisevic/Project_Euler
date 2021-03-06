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

def digit_sum(n):
    return sum(int(i) for i in list(str(n)))

def digit_power_sum():
    powers = []
    for i in range(2, 100):
        for j in range(2, 100):
            power = pow(i, j)
            if power > 9 and digit_sum(power) == i:
                powers.append(power)
    return sorted(powers)[29]

print(digit_power_sum())