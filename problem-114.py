# PROBLEM 114

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
        result = count(n - 1, blocks) # add gray square
        for block in blocks:
            new_size = n - block
            if new_size > 0:
                new_size -= 1 # all blocks must be divided by at least one gray square
            result += count(new_size, blocks)
        return result

def main():
    start = time()
    N = 50
    blocks = tuple(range(3, N + 1))
    resitev = count(N, blocks)
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()