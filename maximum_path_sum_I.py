# By starting at the top of the triangle below and moving to 
# adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#     3
#    7 4
#   2 4 6
#  8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
#        
#                 75
#                95 64
#              17 47 82
#             18 35 87 10
#            20 04 82 47 65
#           19 01 23 75 03 34
#          88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

#_____________________________________________________________________

import time

piramida = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

def najvecja_pot_do(A, i, j, resitve):
    if (i, j) == (0, 0):
        return A[i][j]
    elif i == j and (i, j) != (0, 0):
        return resitve[i - 1, j - 1] + A[i][j] 
    elif j == 0 and i != 0:
        return resitve[i - 1, 0] + A[i][j] 
    else:
        return max(resitve[i - 1, j - 1], resitve[i - 1, j]) + A[i][j]

def main(piramida):
    start = time.time()

    piramida_stevilk = []
    for vrstica in piramida.split('\n'):
        sez = list(map(int, vrstica.split(' ')))
        piramida_stevilk.append(sez)

    slovar_vsot = {}
    for i in range(len(piramida_stevilk)):
        for j in range(len(piramida_stevilk[i])):
            slovar_vsot[i, j] = najvecja_pot_do(
                piramida_stevilk, i, j, slovar_vsot
            )
    ends = []
    for i in range(15):
        ends.append(slovar_vsot[14, i])
    resitev = max(ends)

    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main(piramida)