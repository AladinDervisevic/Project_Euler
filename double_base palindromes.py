# The decimal number, 585 = 1001001001_(2) (binary), 
# is palindromic in both bases.
# Find the sum of all numbers, less than one million, 
# which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, 
# in either base, may not include leading zeros.)
#____________________________________________________

def binary(number):
    binary_number = ''
    while True:
        if number == 1:
            binary_number += '1'
            break
        binary_number += str(number % 2)
        number //= 2
    return binary_number[::-1]

sum = 0
for number in range(1, 10 ** 6):
    binary_num = binary(number)
    if str(number) == str(number)[::-1] and binary_num == binary_num[::-1]:
        sum += number
print(sum)