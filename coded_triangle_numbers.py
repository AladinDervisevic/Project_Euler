# The n^th term of the sequence of triangle numbers is given by, 
# t_n = (1/2)n(n+1); 
# so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its 
# alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
# If the word value is a triangle number then 
# we shall call the word a triangle word.
# Using the added 16K text file containing nearly two-thousand 
# common English words, how many are triangle words?
#______________________________________________________________________

import time
import os

def value(word, values):
    value = 0
    for letter in word:
        value += values.get(letter, 0)
    return value

def main():
    start = time.time()

    os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

    with open('words.txt', encoding = 'utf-8') as file:
        list_of_words = file.read().strip().split(',')

    letter_values = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for number, letter in enumerate(alphabet, 1):
        letter_values[letter] = number
    triangle_numbers = []

    for n in range(1, 1000):
        triangle_numbers.append(n * (n + 1) // 2)

    triangle_words = 0
    for word in list_of_words:
        if value(word, letter_values) in triangle_numbers:
            triangle_words += 1
            
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {triangle_words}\nporabljen cas = {cas}")

main()