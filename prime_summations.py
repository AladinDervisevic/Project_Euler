# It is possible to write 10 as the sum of primes in 
# exactly five different ways:
# 
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# 
# What is the first value which can be written as the sum of primes 
# in over five thousand different ways?
#__________________________________________________________________

from time import time

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

def memo(f):
    slovar = {}
    def mem_f(n, m = 1):
        if (n, m) not in slovar:
            slovar[n, m] = [i for i in f(n, m)]
        return slovar[n, m]
    return mem_f

@memo 
def partitions(n, m = 1):
    if n == 0:
        yield []
    for k in range(m, n + 1):
        for way in partitions(n - k, m = k):
            new_list = [k] + way
            if all(is_prime(i) for i in new_list):
                yield new_list

def main():
    start = time()

    resitev = 1
    while True:
        if len([way for way in partitions(resitev)]) > 5000:
            break
        resitev += 1

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()