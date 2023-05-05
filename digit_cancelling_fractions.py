# The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits 
# in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.
#_____________________________________________________________________________

import time

def test(i, j):
    return i / j == (i // 10) / (j % 10) and str(i)[1] == str(j)[0]

def simplify_and_return_denominator(fraction):
    numerator = fraction[0]
    denominator = fraction[1]
    for i in range(2, numerator + 1):
        if numerator % i == 0 and denominator % i == 0:
            numerator //= i
            denominator //= i
    return denominator

def main():
    start = time.time()

    eligible_fractions = []
    for i in range(10, 100):
        for j in range(10, 100):
            if i % 10 != 0 and j % 10 != 0 and test(i, j) and i < j:
                eligible_fractions.append((i, j))
    print(eligible_fractions)

    answer = [1,1]
    for fraction in eligible_fractions:
        answer[0] *= (fraction[0] // 10)
        answer[1] *= (fraction[1] % 10)

    answer = simplify_and_return_denominator(answer)

    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {answer}\nporabljen cas = {cas}")

main()