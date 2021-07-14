# Consider the fraction, n/d, where n and d are positive integers. 
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 
# in ascending order of size, we get:
# 
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
#  5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set 
# of reduced proper fractions for d ≤ 1,000,000?
#__________________________________________________________________

# Euler's totient function : 
# fi(n) = n * PI_(p|n) (1 - 1/p) = n * (1 - 1/p_1) *...* (1 - 1/p_m), 
# where p_1, ... , p_m are prime factors of n.

fi = [i for i in range(10 ** 6 + 1)]
for i in range(2, 10 ** 6 + 1):
    if fi[i] == i:
        for j in range(i, 10 ** 6 + 1, i):
            fi[j] = (fi[j] / i) * (i - 1)
result = int(sum(fi)) - 1
print(result)