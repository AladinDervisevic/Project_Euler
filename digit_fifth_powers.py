# Surprisingly there are only three numbers that can be written 
# as the sum of fourth powers of their digits:
# 1634 = 1 ** 4 + 6 ** 4 + 3 ** 4 + 4 ** 4
# 8208 = 8 ** 4 + 2 ** 4 + 0 ** 4 + 8 ** 4
# 9474 = 9 ** 4 + 4 ** 4 + 7 ** 4 + 4 ** 4
# As 1 = 1 ** 4 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written 
# as the sum of fifth powers of their digits.
#_______________________________________________________________

def vsota_potenc(stevilo, k = 5):
    if stevilo <= 9:
        return stevilo ** k
    else:
        return (stevilo % 10) ** k + vsota_potenc(stevilo // 10, k)

vsota = 0
for stevilo in range(1, 1000000):
    if stevilo == vsota_potenc(stevilo) and vsota_potenc(stevilo) != 1:
        vsota += stevilo
print(vsota)