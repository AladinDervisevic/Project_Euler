# The decimal number, 585 = 1001001001_(2) (binary), 
# is palindromic in both bases.
# Find the sum of all numbers, less than one million, 
# which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, 
# in either base, may not include leading zeros.)
#____________________________________________________

import time

def is_binary_palindrome(number):
    binary_number = ''
    while True:
        if number == 1:
            binary_number += '1'
            break
        binary_number += str(number % 2)
        number //= 2
    return binary_number == binary_number[::-1]

def get_decimal_palindromes():
    palindromes = set()
    for i in range(1, 10):
        palindromes.add(i)
        palindromes.add(i * 11)
        for j in range(10):
            palindromes.add(i * 101 + j * 10)
            palindromes.add(i * 1001 + j * 110)
            for k in range(10):
                palindromes.add(i * 10001 + j * 1010 + k * 100)
                palindromes.add(i * 100001 + j * 10010 + k * 1100)
    return palindromes

def main():
    start = time.time()

    sum = 0
    candidates = get_decimal_palindromes()
    for i in candidates:
        if is_binary_palindrome(i):
            sum += i

    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {sum}\nporabljen cas = {cas}")

main()