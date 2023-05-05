# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers 
# are all figurate (polygonal) numbers and are generated 
# by the following formula:
#
# Triangle	 	P_3,n = n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Square	 	P_4,n = n ** 2	 	    1, 4, 9, 16, 25, ...
# Pentagonal	P_5,n = n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	P_6,n = n(2n−1)	 	    1, 6, 15, 28, 45, ...
# Heptagonal	P_7,n = n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Octagonal	 	P_8,n = n(3n−2)	 	    1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, 
# has three interesting properties.
# 1) The set is cyclic, in that the last two digits of each number 
# is the first two digits of the next number 
# (including the last number with the first).
# 2) Each polygonal type: triangle (P_3,127 = 8128), square (P_4,91 = 8281), 
# and pentagonal (P_5,44 = 2882), 
# is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers 
# for which each polygonal type: 
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
# is represented by a different number in the set.
#____________________________________________________________________________
from itertools import permutations
import time

def is_triangle(n):
    return len(str(n * (n + 1) // 2)) == 4

def is_square(n):
    return len(str(n ** 2)) == 4

def is_pentagonal(n):
    return len(str(n * (3 * n - 1) // 2)) == 4

def is_hexagonal(n):
    return len(str(n * (2 * n - 1))) == 4

def is_heptagonal(n):
    return len(str(n * (5 * n - 3) // 2)) == 4

def is_octagonal(n):
    return len(str(n * (3 * n - 2))) == 4

def cyclical_figurate_numbers():
    triangle = [n * (n + 1) // 2 for n in range(1, 200) if is_triangle(n)]
    square = [n ** 2 for n in range(1, 200) if is_square(n)]
    pentagonal = [
        n * (3 * n - 1) // 2 for n in range(1, 200) if is_pentagonal(n)
    ]
    hexagonal = [n * (2 * n - 1) for n in range(1, 200) if is_hexagonal(n)]
    heptagonal = [
        n * (5 * n - 3) // 2 for n in range(1, 200) if is_heptagonal(n)
    ]
    octagonal = [n * (3 * n - 2) for n in range(1, 200) if is_octagonal(n)]
    triangles = {}
    squares = {}
    pentagonals = {}
    hexagonals = {}
    heptagonals = {}
    octagonals = {}
    for i in triangle:
        triangles[i // 100] = i % 100
    for i in square:
        squares[i // 100] = i % 100
    for i in pentagonal:
        pentagonals[i // 100] = i % 100
    for i in hexagonal:
        hexagonals[i // 100] = i % 100
    for i in heptagonal:
        heptagonals[i // 100] = i % 100
    for i in octagonal:
        octagonals[i // 100] = i % 100
    figures = [squares, pentagonals, hexagonals, heptagonals, octagonals]
    combos = list(permutations(figures))
    for num in triangles:
        for combo in combos:
            k = num
            v = triangles.get(num)
            numbers = [(k, v)]
            for fig in combo:
                k, v = v, fig.get(v, -1)
                if v == -1:
                    break
                numbers.append((k, v))
            if len(numbers) == 6 and numbers[0][0] == numbers[-1][-1]: 
                result = numbers
    return sum(i * 100 + j for i, j in result)

def main():
    start = time.time()
    resitev = cyclical_figurate_numbers()
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()