# PROBLEM 116

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
def rgb(n, block): # n = number of blocks
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return rgb(n - 1, block) + rgb(n - block, block)

def main():
    start = time()
    N = 50
    resitev = sum(rgb(N, i) - 1 for i in range(2, 5)) # -1 cuz each call counts the empty row
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()