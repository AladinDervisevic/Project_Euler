# The number 145 is well known for the property that the sum of the factorial 
# of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain 
# of numbers that link back to 169; 
# it turns out that there are only three such loops that exist:
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will 
# eventually get stuck in a loop. For example,
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms,
# but the longest non-repeating chain with a starting number 
# below one million is sixty terms.
# How many chains, with a starting number below one million, 
# contain exactly sixty non-repeating terms?
#_____________________________________________________________________________
from time import time
from math import factorial

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
def next_in_chain(number):
    return sum(factorial(int(i)) for i in str(number))
    
def main():
    start = time()
    N = 10 ** 6
    terms = {}
    
    for i in range(N):
        n = i
        rec_stack = set()
        while True:
            if n in rec_stack:
                terms[i] = len(rec_stack)
                break
            rec_stack.add(n)
            n = next_in_chain(n)
            if n in terms:
                terms[i] = len(rec_stack) + terms[n]
                break
        
    resitev = sum(1 for v in terms.values() if v == 60)

    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")
    

main()