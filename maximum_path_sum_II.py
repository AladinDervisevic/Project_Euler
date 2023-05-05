# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in the given text file, 
# containing a triangle with one-hundred rows.
#___________________________________________________________________________
import os
import time

def najvecja_pot_do(A, i, j, resitve):
    if (i, j) == (0, 0):
        return A[i][j]
    elif i == j and (i, j) != (0, 0):
        return resitve[i - 1, j - 1] + A[i][j] 
    elif j == 0 and i != 0:
        return resitve[i - 1, 0] + A[i][j] 
    else:
        return max(resitve[i - 1, j - 1], resitve[i - 1, j]) + A[i][j]

def najvecja_pot_slovar(A):
    slovar_vsot = {}
    for i in range(len(A)):
        for j in range(len(A[i])):
            slovar_vsot[i, j] = najvecja_pot_do(A, i, j, slovar_vsot)
    ends = []
    for i in range(100):
        ends.append(slovar_vsot[99, i])
    return max(ends)

def main():
    start = time.time()

    os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')
    with open('triangle.txt', encoding = 'utf-8') as file:
        vrstice = file.read().strip().split('\n')

    piramida = []
    for i in vrstice:
        vrstica = [int(j) for j in i.split(' ')]
        piramida.append(vrstica)

    resitev = najvecja_pot_slovar(piramida)

    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()