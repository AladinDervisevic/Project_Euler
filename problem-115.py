# PROBLEM 115

from time import time

def memo(f):
    result = {}
    def memo_f(*args, **kwargs):
        if args not in result:
            result[args] = f(*args, **kwargs)
        # else:
        #     print("  reusing", args, "=", result[args])
        return result[args]
    return memo_f

@memo
def count(n, blocks): # n = number of blocks
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        result = count(n - 1, blocks) # add black square
        for block in blocks:
            new_size = n - block
            if new_size > 0:
                new_size -= 1 # all blocks must be divided by at least one black square
            result += count(new_size, blocks)
        return result

def main():
    start = time()
    N, M = 50, 50 # length, min block size
    while True:
        blocks = tuple(range(M, N + 1))
        if count(N, blocks) > 10 ** 6:
            break
        N += 1
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {N}\nporabljen cas = {cas}")

main()