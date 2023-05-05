# The series, 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 10 ** 10 = 10405071317.
# Find the last ten digits of the series, 
# 1 ** 1 + 2 ** 2 + 3 ** 3 + ... + 1000 ** 1000.
#_____________________________________________________________________

from time import time

def main():
    start = time()
    resitev = sum(i ** i for i in range(1, 1001)) % 10 ** 10
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()