# In the 5 by 5 matrix below, the minimal path sum from 
# the top left to the bottom right, by only moving to the right and down, 
# is indicated with $ and is equal to 2427.
#   131$ 673  234  103  18
#   201$ 96$  342$ 965  150
#   630  803  746$ 422$ 111
#   537  699  497  121$ 956
#   805  732  524  37$  331$
# Find the minimal path sum from top left to the bottom right by only moving 
# right and down in the given 80x80 matrix in the matrix.txt document.
#___________________________________________________________________________
import os
from time import time

def local_min_path_sum(matrix, i, j, dictionary_of_sums):
    if i == 0 and j == 0:
        return matrix[0][0]
    elif i == 0:
        return dictionary_of_sums[i, j - 1] + matrix[i][j]
    elif j == 0:
        return dictionary_of_sums[i - 1, j] + matrix[i][j]
    else:
        return min(
            dictionary_of_sums[i - 1, j], dictionary_of_sums[i, j - 1]
            ) + matrix[i][j]

# finds the minimum path sum from start to end as wanted in the task
def min_path_sum(matrix):
    dictionary_of_sums = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dictionary_of_sums[i, j] = local_min_path_sum(
                matrix, i, j, dictionary_of_sums
            )
    return dictionary_of_sums[len(matrix) - 1, len(matrix[0]) - 1]

def main():
    start = time()
    os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

    with open('matrix.txt', encoding = 'utf-8') as file:
        rows = file.read().strip().split('\n')
        mat = []
        for i in rows:
            row = [int(j) for j in i.split(',')]
            mat.append(row)
    
    resitev = min_path_sum(mat)

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()