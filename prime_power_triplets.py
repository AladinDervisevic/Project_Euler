# The smallest number expressible as the sum of a prime square, 
# prime cube, and prime fourth power is 28. 
# In fact, there are exactly four numbers below fifty, 
# that can be expressed in such a way:

# 28 = 2 ** 2 + 2 ** 3 + 2 ** 4
# 33 = 3 ** 2 + 2 ** 3 + 2 ** 4
# 49 = 5 ** 2 + 2 ** 3 + 2 ** 4
# 47 = 2 ** 2 + 3 ** 3 + 2 ** 4

# How many numbers below fifty million can be expressed as 
# the sum of a prime square, prime cube, and prime fourth power?
#________________________________________________________________

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

def main():
    start = time()

    numbers = set()
    primes = primes_up_to(int((5 * 10 ** 7) ** 0.5))
    for i in primes:
        if i ** 2 >= 5 * 10 ** 7:
            break
        for j in primes:
            if i ** 2 + j ** 3 >= 5 * 10 ** 7:
                break
            for k in primes:
                n = i ** 2 + j ** 3 + k ** 4
                if n < 5 * 10 ** 7:
                    numbers.add(n)
                else:
                    break
    
    resitev = len(numbers)
    end = time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()