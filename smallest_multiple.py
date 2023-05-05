# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#__________________________________________________________________________________________________________

from time import time

def main():
    start = time()

    resitev = 2 * 7 * 11 * 13 * 17 * 18 * 19 * 20
    for i in range(resitev, 10 ** 10):
        if all(i % j == 0 for j in range(1, 21)):
            resitev = i
            break
        
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()