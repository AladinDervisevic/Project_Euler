import math

# A Pythagorean triplet is a set of three natural numbers, 
# a < b < c, for which, a ** 2 + b ** 2 = c ** 2
# For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a * b * c.
#_________________________________________________________________________

def special_pythagorean_triplet():
    product = 0
    for a in range(1,300):
        for b in range(1,400):
            if a < b:
                c = math.sqrt(a ** 2 + b ** 2)
                if a + b + c == 1000:
                    product = int(a * b * c)
                    return product

print(special_pythagorean_triplet())