# Using names.txt a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to 
# obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?
#_________________________________________________________________________
import os
from time import time

def score(name, values):
    sum = 0
    for letter in name:
        sum += values.get(letter, 0)
    return sum

def main():
    start = time()
    os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

    with open('names.txt', encoding='utf-8') as file:
        names = file.read().strip().split(',')
    names.sort()
    letter_value = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i, letter in enumerate(alphabet, 1):
        letter_value[letter] = i
    total = sum(
        score(name, letter_value) * i  for i, name in enumerate(names, 1)
    )
    
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {total}\nporabljen cas = {cas}")

main()