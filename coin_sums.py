# In the United Kingdom the currency is made up of pound (£) and pence (p). 
# There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
#__________________________________________________________________________

# Discrete mathematics --> Stirling's numbers of 2nd kind

coins = [200, 100, 50, 20, 10, 5, 2, 1]
money = 200

def count(money, coins):
    if money == 0:
        return 1
    if money <= 0 or len(coins) == 0:
        return 0
    return count(money, coins[1:]) + count(money - coins[0], coins)

print(count(money, coins))    