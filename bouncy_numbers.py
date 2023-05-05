# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy.
# In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
# Find the least number for which the proportion of bouncy numbers is exactly 99%.
#_________________________________________________________________________________

from time import time

def is_bouncy(n):
    n = str(n)
    increasing = ''.join(sorted(n))
    decreasing = increasing[::-1]
    return n != increasing and n != decreasing

def main():
    start = time()
    bouncy_percentage, bouncy_counter = 0.9, 21780 * 0.9
    number = 21780
    while bouncy_percentage != 0.99:
        number += 1
        if is_bouncy(number):
            bouncy_counter += 1
            bouncy_percentage = bouncy_counter / number
    end = time()
    cas = round(end - start, 2)
    print(f'resitev = {number}\nporabljen cas = {cas}')

main()