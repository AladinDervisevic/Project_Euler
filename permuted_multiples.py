# It can be seen that the number, 125874, and its double, 251748, 
# contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
# contain the same digits.
#_________________________________________________________________________
from itertools import permutations

def permuted_multiples():
    for i in range(100, 10 ** 6):
        perm_numbers = []
        for perm in list(permutations(str(i))):
            if perm[0] != '0':
                perm_numbers.append(int(''.join(perm)))
        if all(j * i in perm_numbers for j in range(1, 7)):
            return i

print(permuted_multiples())

# Little slow, but finishes under 20s.