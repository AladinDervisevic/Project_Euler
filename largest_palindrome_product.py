# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers 
# is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#__________________________________________________________________________

import time

def largest_palindrome():
    palindromes = []
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                palindromes.append(10001 * i + 1010 * j + 100 * k)
                palindromes.append(100001 * i + 10010 * j + 1100 * k)
    max_pal = 0
    for i in range(100, 1000):
        for pal in palindromes:
            if pal % i == 0 and 100 <= pal // i < 1000:
                max_pal = max(max_pal, pal)
    return max_pal
            

def main():
    start = time.time()
    resitev = largest_palindrome()
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()