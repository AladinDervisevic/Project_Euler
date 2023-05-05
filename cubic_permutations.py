# The cube, 41063625 (345 ** 3), can be permuted to produce two other cubes: 
# 56623104 (384 ** 3) and 66430125 (405 ** 3). 
# In fact, 41063625 is the smallest cube which has exactly three permutations 
# of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits 
# are cube.
#_____________________________________________________________________________

import time

def is_cube(n):
    if n <= 1:
        return False
    return n == pow(round(n ** (1 / 3)), 3)

def wanted_cube():
    cubes = {}
    i = 1
    while True:
        key = ''.join(sorted(str(i ** 3)))
        if key not in cubes:
            cubes[key] = [i]
        else:
            cubes[key].append(i)
        if len(cubes[key]) == 5:
            return min(i ** 3 for i in cubes[key])
        i += 1

def main():
    start = time.time()
    resitev = wanted_cube()
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()