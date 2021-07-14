# By replacing the 1st digit of the 2-digit number *3, it turns out that 
# six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, 
# this 5-digit number is the first example having seven primes 
# among the ten generated numbers, yielding the family: 
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, 
# is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number 
# (not necessarily adjacent digits) with the same digit, 
# is part of an eight prime value family.
#_____________________________________________________________________________
# Replacing a number's last digit is not needed since in any numbers case 
# it'll have 5 generated numbers, divisible by 2.

def is_prime(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True

def get_primes(n):
    # returns a list of all primes < n
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: 2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

def prime_family_value(prime):
    rep = [i for i in str(prime) if str(prime).count(i) == 3][0]
    indexes_of_rep = [
        i for i in range(len(str(prime))) if str(prime)[i] == rep
    ]
    primes = []
    for digit in range(10):
        number = list(str(prime))
        for index in indexes_of_rep:
            number[index] = str(digit)
        number = int(''.join(number))
        if len(str(number)) == len(str(prime)) and is_prime(number):
            primes.append(number)
    return len(primes)

def out():
    primes = set(get_primes(10 ** 7)) - set(get_primes(10 ** 4))
    for prime in sorted(primes):  
        if any(str(prime).count(digit) == 3 for digit in str(prime)):
            rep = [i for i in str(prime) if str(prime).count(i) == 3][0]
            if str(prime)[-1] == rep:
                continue    # last digit can't be the repeating one
            if prime_family_value(prime) == 8:
                return prime
    return 'Error 404'

print(out())