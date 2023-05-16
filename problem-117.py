# PROBLEM 117

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
def rgb(n, blocks = (1, 2, 3, 4)): # n = number of blocks
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(rgb(n - k) for k in blocks)

def main():
    start = time()
    N = 50
    resitev = rgb(N)
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()