# By counting carefully it can be seen that a rectangular grid measuring 
# 3 by 2 contains eighteen rectangles.
# Although there exists no rectangular grid that contains 
# exactly two million rectangles,
# find the area of the grid with the nearest solution.
#________________________________________________________________________

# sum of the first (a) numbers multiplied by the sum of the first (b) numbers

limit = 2 * 10 ** 6
area = 0
min_difference = limit
for a in range(1, 101):
    for b in range(a, 101):
        number_of_rectangles = (a ** 2 + a) * (b ** 2 + b) // 4
        difference = abs(limit - number_of_rectangles)
        if difference < min_difference:
            min_difference = difference
            area = a * b
print(area)