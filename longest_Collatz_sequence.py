# The following iterative sequence is defined for 
# the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, 
# we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) 
# contains 10 terms.
# Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
#___________________________________________________________________________

import time

def chain_length(n, lengths):
    if n in lengths:
        return lengths[n]
    if n % 2 == 0:
        lengths[n] = 1 + chain_length(n // 2, lengths)
    else:
        lengths[n] = 2 + chain_length((3 * n + 1) // 2, lengths)
    return lengths[n]

def longest_collatz_sequence():
    lengths = {1: 1}
    max_len, result = 0, 0
    for i in range(1, 10 ** 6):
        len_i = chain_length(i, lengths)
        if len_i > max_len:
            max_len = len_i
            result = i
    return result

def main():
    start = time.time()
    resitev = longest_collatz_sequence()
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()