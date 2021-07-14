# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120 :
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p <= 1000, is the number of solutions maximised?
#_____________________________________________________________________________

# Euclid's formula for generating Pythagorean triples 
# given an arbitrary pair of integeres m & n, m > n > 0.

def euclid():
    Pythagorean_triples = {}
    for a in range(1, 500):
        for b in range(1, 500):
            c = (a ** 2 + b ** 2) ** 0.5
            if a > b and float(c) == int(c):
                perimeter = a + b + int(c)
                if perimeter <= 1000:
                    if perimeter not in Pythagorean_triples:
                        Pythagorean_triples[perimeter] = 1
                    elif perimeter in Pythagorean_triples:
                        Pythagorean_triples[perimeter] += 1
    return max((v, k) for k, v in Pythagorean_triples.items())[1]

print(euclid())