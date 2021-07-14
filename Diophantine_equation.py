# Consider quadratic Diophantine equations of the form:
# x ** 2 – D * y ** 2 = 1
# For example, when D = 13, the minimal solution in x is 
# 649 ** 2 – 13 × 180 ** 2 = 1.
# It can be assumed that there are no solutions 
# in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, 
# we obtain the following:
# 
# 3 ** 2 – 2 × 2 ** 2 = 1
# 2 ** 2 – 3 × 1 ** 2 = 1
# 9 ** 2 – 5 × 4 ** 2 = 1
# 5 ** 2 – 6 × 2 ** 2 = 1
# 8 ** 2 – 7 × 3 ** 2 = 1
# 
# Hence, by considering minimal solutions in x for D ≤ 7, 
# the largest x is obtained when D=5.
# Find the value of D ≤ 1000 in minimal solutions of x 
# for which the largest value of x is obtained.
#____________________________________________________________

# After some research, I found out about these topics, in this order: 
# Diophnantine equations -> Pell's equation -> Chakravala method
# and implemented continued fractions.
# https://en.wikipedia.org/wiki/Pell%27s_equation
# https://en.wikipedia.org/wiki/Continued_fraction
# https://en.wikipedia.org/wiki/Chakravala_method 

def is_square(number):
    return int(number ** 0.5) ** 2 == int(float(number ** 0.5) ** 2)

def closest_square(number):
    up = number + 1
    down = number - 1
    while True:
        if is_square(up):
            return up
        if is_square(down):
            return down
        up += 1
        down += 1

def get_new_values(x, y, k, m, D):
    new_x = (x * m + D * y) // abs(k)
    new_y = (x + y * m) // abs(k)
    new_k = (m ** 2 - D) // k
    return (new_x, new_y, new_k)

def Diophantine():
    result_D = 0
    result_x = 0
    candidates = sorted(
        set(range(2, 1001)) - set(i ** 2 for i in range(2, 101))
    )
    for D in candidates:  # the formula : x ** 2 - D * y ** 2 == k
        x, y = int(closest_square(D) ** 0.5), 1
        k = x ** 2 - D * y ** 2
        while k != 1:
            valid_m = []
            for m in range(1, 101):
                if (x + y * m) % k == 0:
                    valid_m.append((abs(m ** 2 - D), m))
            m = min(valid_m)[1]
            x, y, k = get_new_values(x, y, k, m, D)
        if x > result_x:
            result_x = x
            result_D = D
    return result_D

print(Diophantine())