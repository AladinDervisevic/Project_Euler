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
from math import factorial

def next_in_chain(number):
    if number < 10:
        return factorial(number)
    else:
        return factorial(number % 10) + next_in_chain(number // 10)

chains_with_sixty_non_repeating_terms = 0
for number in range(10 ** 6):
    terms, last_number = [number], number
    while True:
        last_number = next_in_chain(last_number)
        if last_number not in terms:
            terms.append(last_number)
        else:
            break
    if len(terms) == 60:
        chains_with_sixty_non_repeating_terms += 1
print(chains_with_sixty_non_repeating_terms)

# Runtime : 1min 50s