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
os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

def score(name, values):
    sum = 0
    for letter in name:
        sum += values.get(letter, 0)
    return sum

with open('names.txt', encoding='utf-8') as file:
    names = file.read().strip().split(',')
names.sort()
letter_score = {}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in alphabet:
    letter_score[letter] = alphabet.index(letter) + 1
total = sum(
    score(name, letter_score) * i  for i, name in enumerate(names, 1)
)
print(total)