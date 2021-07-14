# The minimal path sum in the 5 by 5 matrix below, by starting in any cell 
# in the left column and finishing in any cell in the right column, 
# and only moving up, down, and right,
#  is indicated with $; the sum is equal to 994.
# 131  673  234$ 103$ 18$
# 201$ 96$  342$ 965  150
# 630  803  746  422  111
# 537  699  497  121  956
# 805  732  524  37   331
# Find the minimal path sum from the left column to the right column 
# in the given 80 x 80 matrix.
#_________________________________________________________________________
import os
os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

def min_path_sum_3ways(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    min_path = [matrix[i][0] for i in range(rows)] # the entire first column aka where you start
    for j in range(1, cols):
        column = [matrix[i][j] for i in range(rows)] # produces the entire next column 
        min_path = [ 
                    column[i] +  # value of the cell you're in + 
                    min(        # value of the smallest path to that cell
                        [ min_path[prev_row] +  
                        sum(
                            column[prev_row : i : (1 if prev_row <= i else -1)]
                        )
                        for prev_row in range(rows) ]
                    ) 
                    for i in range(rows)  # for every cell/row in that column from top to bottom
        ]
    return min(min_path) # the smallest of the paths up to the cells in the last column

with open('matrix.txt', encoding = 'utf-8') as file:
    rows = file.read().strip().split('\n')
    mat = []
    for i in rows:
        row = [int(j) for j in i.split(',')]
        mat.append(row)

print(min_path_sum_3ways(mat))