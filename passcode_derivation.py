# A common security method used for online banking is to ask the user 
# for three random characters from a passcode. For example, 
# if the passcode was 531278, they may ask for the 2nd, 3rd, 
# and 5th characters; the expected reply would be: 317.
# You're given fifty successful login attempts.
# Given that the three characters are always asked for in order, 
# analyse the file so as to determine 
# the shortest possible secret passcode of unknown length.
#____________________________________________________________________

# note1 : there is no digit 4 or 5, so the number will be a permutation of 123_567890
# note2 : 0 isn't a 1st or 2nd digit in any of the login attempts,which means 0 is at the end

import os
os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

with open('keylog.txt', encoding = 'utf-8') as file:
    login_attempts = file.read().rstrip().split('\n')

for i in range(len(login_attempts)):
    login_attempts[i] = int(login_attempts[i])

logins = []
for attempt in login_attempts:
    if attempt not in logins:
        logins.append(attempt)
slovar = {}
for i in {1, 2, 3, 6, 7, 8, 9}:    # not checking for 0 cuz note2 nor 4,5 cuz note1
    digits_ocurring_after_i = set()
    for num in logins:
        if num // 100 == i:
            digits = f'{num % 100}'
            for digit in digits:
                digits_ocurring_after_i.add(int(digit))
    slovar[i] = len(digits_ocurring_after_i) # key = digit in code, value = how many other digits occur after it
inverted_slovar = []
for k, v in slovar.items():
    inverted_slovar.append((v, k))
passcode = ''
for pair in sorted(inverted_slovar, reverse=True):  # descending order of digits in code
    passcode += f'{pair[1]}'
print(int(passcode + '0'))  # added 0 at the end ofc