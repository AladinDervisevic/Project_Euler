# It is possible to write five as a sum in exactly six different ways:
# 
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# 
# How many different ways can one hundred be written as a sum of 
# at least two positive integers?
#______________________________________________________________________

# KEY : Partitions / razclenitve pri Diskretni matematiki 1
# let P_k(n,k) be the number of partitions of the integer n by k components.
# let P(n) be the number of all valid partitions of the integer
# Partitions are not ordered, thus : 1 + 3 = 3 + 1 is counted once.

def memo(P):
    slovar = {}
    def mem_P(n, k):
        if (n, k) not in slovar:
            slovar[n, k] = P(n, k)
        return slovar[n, k]
    return mem_P

@memo
def P_k(n, k):
    if k > n or (k == 0 and n > 0):
        return 0
    if n == k == 0:
        return 1
    return P_k(n - 1, k - 1) + P_k(n - k, k)

def P(n):
    return sum(P_k(n, k) for k in range(2, n + 1))

print(P(100))