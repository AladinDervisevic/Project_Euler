# PROBLEM 123

from time import time

def primes_up_to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """Returns a list of all primes p <= n."""
    if n < 2:
        return []
    elif n < 3:
        return [2]
    elif n < 5:
        return [2, 3]
    elif n < 6:
        return [2, 3, 5]
    else:
        n += 1
    correction = n % 6 > 1
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n // 3)
    sieve[0] = False
    m = int(n ** 0.5) // 3
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = [False] * ((n // 6 - (k * k) // 6 - 1) // k + 1)
            m = (k * k + 4 * k - 2 * k * (i & 1))
            sieve[m // 3::2 * k] = [False] * ((n // 6 - m // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]

# https://en.wikipedia.org/wiki/Binomial_theorem
def remainder(p, n):
    return (2 * n * p) % (p ** 2)

def main():
    start = time()
    resitev = 0
    LIMIT = 10 ** 10
    
    primes = primes_up_to(10 ** 6)
    primes = [primes[i] for i in range(len(primes)) if i % 2 == 0] # odd primes
    candidates = list(enumerate(primes))
    
    for i, p in candidates:
        n = 2 * i + 1
        if remainder(p, n) > LIMIT:
            resitev = n
            break
        
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()