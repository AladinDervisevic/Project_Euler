# PROBLEM 80

from time import time
import decimal

def main():
    start = time()

    resitev = 0
    decimal.getcontext().prec = 110
    candidates = set(range(1, 100)) - set(i ** 2 for i in range(1, 10))
    for n in candidates:
        d = decimal.Decimal(n)
        d = d.sqrt()
        d = str(d).replace('.', '')
        resitev += sum(int(i) for i in d[:100])

    end = time()
    cas = round(end - start, 2)
    print(f'resitev = {resitev}\nporabljen cas = {cas}')

main()