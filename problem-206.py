# PROBLEM 206

from time import time
from math import ceil, floor

def proper_form(candidate, FORM):
    for i in range(0, 19, 2):
        if str(candidate)[i] != FORM[i]:
            return False
    return True

# only if you square numbers that have a zero at the end, do you get a zero at the end again,
# but the previous digit of last is also a zero (in the squared number)

def main():
    start = time()
    resitev = None
    FORM = [None] * 19
    FORM[-1] = '0'
    
    for i in range(0, 17, 2):
        FORM[i] = f'{i // 2 + 1}'
        
    MIN, MAX = FORM[::], FORM[::]
        
    for i in range(1, 18, 2):
        MIN[i] = '0'
        MAX[i] = '9'
        
    MIN = floor(int(''.join(MIN)) ** 0.5) 
    MAX = ceil(int(''.join(MAX)) ** 0.5)
    
    while MAX % 10 != 0:
        MAX += 1
    
    for root in range(MAX, MIN, -10):
        if proper_form(root ** 2, FORM):
            resitev = root
            break
    
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()