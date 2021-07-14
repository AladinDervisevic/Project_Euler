# It turns out that 12 cm is the smallest length of wire that can be bent 
# to form an integer sided
# right angle triangle in exactly one way, but there are many more examples.
# 
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# 
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form 
# an integer sided right angle triangle, 
# and other lengths allow more than one solution to be found.
# For example, using 120 cm it is possible to form exactly three 
# different integer sided right angle triangles.
# 
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# 
# Given that L is the length of the wire, for how many values of 
# L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
#_____________________________________________________________________________
from math import gcd

candidates, non_valids = set(), set()
limit = int((1500000 / 2) ** 0.5)
for m in range(2, limit):
    for n in range(1, m):
        if (m + n) % 2 == 1 and gcd(m, n) == 1:
            a, b, c = m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
            wire = a + b + c
            while wire <= 1500000:
                if wire not in candidates:
                    candidates.add(wire)
                else:
                    non_valids.add(wire)
                wire += a + b + c
result = len(candidates - non_valids)
print(result)