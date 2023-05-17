# Let r be the remainder when (a − 1) ** n + (a + 1) ** n 
# is divided by a ** 2.
# For example, if a = 7 and n = 3, then r = 42: 
# 6 ** 3 + 8 ** 3 = 728 ≡ 42 (mod 49).
# And as n varies, so too will r, 
# but for a = 7 it turns out that r_max = 42.
# For 3 ≤ a ≤ 1000, find ∑ r_max.
#_________________________________________________________

# https://en.wikipedia.org/wiki/Binomial_theorem

# For any a & any even n, the remainder will always be 2.
# For any a & any odd n, it'll be 2 * a * n.
# I need 2 * n to be as close to a as possible

from time import time

def main():
    start = time()
    resitev = 0
    for a in range(3, 1001):
        resitev += max((2 * n * a) % (a ** 2) for n in range(a // 2 + 1))
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()