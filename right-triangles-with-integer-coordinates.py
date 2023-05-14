# The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates 
# and are joined to the origin, O(0,0), to form ΔOPQ.
# There are exactly fourteen triangles containing a right angle that 
# can be formed when each co-ordinate lies between 0 and 2 inclusive; 
# that is 0 ≤ x1, y1, x2, y2 ≤ 2.
# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
#_____________________________________________________________________________

from time import time

def is_right(x1, y1, x2, y2):
    a = x1 ** 2 + y1 ** 2
    b = x2 ** 2 + y2 ** 2
    c = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return c == a + b or b == a + c or a == b + c

def main():
    N = 50
    start = time()
    pravi = set()
    
    for x1 in range(1, N + 1): # N^2
        for y2 in range(1, N + 1):
            pravi.add((x1, 0, 0, y2)) # pravi kot pri (0,0)

    for x1 in range(1, N + 1): # 2 * N^2
        y1, x2 = 0, x1         # pravi kot na x ali y osi
        for y2 in range(1, N + 1):
            pravi.add((x1, y1, x2, y2))
            pravi.add((y1, x1, y2, x2))
            
    for x1 in range(1, N + 1):
        for y1 in range(x1 + 1):
            for x2 in range(N + 1):
                for y2 in range(y1 + 1, N + 1):
                    par = (x1, y1, x2, y2)
                    zrcalni_par = (y1, x1, y2, x2)
                    obratni_par = (x2, y2, x1, y1)
                    if is_right(x1, y1, x2, y2):
                        if par not in pravi and obratni_par not in pravi:
                            pravi.add(par)
                            pravi.add(zrcalni_par)
                
    resitev = len(pravi)
    end = time()
    cas = round(end - start, 2)
    print(f'resitev = {resitev}\nporabljen cas = {cas}')

main()