def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


def sqrt(n):
    m = int(n ** 0.5)
    if m ** 2 == n:
        return m
    elif (m + 1) ** 2 == n:
        return (m + 1)


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


def factorize(n, primes=None):
    if primes is None:
        primes = primes_up_to(int(n ** 0.5))
    factors = {}
    for p in primes:
        if p ** 2 > n:
            break
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k > 0:
            factors[p] = k
    if n > 1:
        factors[n] = 1
    return factors


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    a %= m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def is_square(n):
    return int(n ** 0.5) ** 2 == n


def memo(f):
    result = {}
    def memo_f(*args, **kwargs):
        if args not in result:
            result[args] = f(*args, **kwargs)
        # else:
        #     print("  reusing", args, "=", result[args])
        return result[args]
    return memo_f


def is_prime(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True


def is_probable_prime(n, witnesses=[2, 7, 61]):
    if n <= 2 or n % 2 == 0:
        return n == 2
    if n in witnesses:
        return True
    # write n - 1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  # n is definitely composite

    for a in witnesses:
        if try_composite(a):
            return False
    return True


@memo
def combinations(n, k):
    if k == 0:
        return [[]]
    elif n < k:
        return []
    else:
        return [c + [r] for r in range(k - 1, n) for c in combinations(r, k - 1)]


def subsets(a, k):
    a = list(a)
    for c in combinations(len(a), k):
        yield {a[i] for i in c}


def all_subsets(x):
    x = x.copy()
    if x:
        a = x.pop()
        for y in all_subsets(x):
            yield y
            yield y | {a}
    else:
        yield set()


def totient(n, primes=None):
    factors = factorize(n, primes)
    tot = n
    for p in factors:
        tot //= p
        tot *= p - 1
    return tot


def log(n, b):
    l = 0
    while n >= b:
        l += 1
        n //= b
    return l


def possible_products(pairs, minimum, maximum):
    if pairs:
        p, n = pairs[0]
        rest_pairs = pairs[1:]
        pk = 1
        for k in range(0, n + 1):
            for prod in possible_products(rest_pairs, minimum // pk, maximum // pk):
                d = pk * prod
                if d >= minimum:
                    yield d
            pk *= p
    elif maximum >= 1 >= minimum:
        yield 1


def divisors(n, primes=None):
    # factors = 
    for p in possible_products(tuple(factorize(n, primes).items()), 1, n):
        yield p

# def count_permutations(lst):
#     perms = 1
#     current_x = None
#     current_count = 0
#     for n, x in enumerate(lst):
#         perms *= n + 1
#         if x == current_x:
#             current_count += 1
#             perms //= current_count
#         else:
#             current_x = x
#             current_count = 1
#     return perms


def collect(lst):
    collected = {}
    for x in lst:
        collected[x] = collected.get(x, 0) + 1
    return collected


def count_perms(pairs):
    n = 1
    perms = 1
    for _, occurrences in pairs:
        for k in range(1, occurrences + 1):
            perms *= n
            perms //= k
            n += 1
    return perms


def count_permutations(lst):
    return count_perms(collect(lst).items())

def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
