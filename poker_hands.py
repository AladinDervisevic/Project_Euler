# In the card game poker, a hand consists of five cards and are ranked, 
# from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank 
# made up of the highest value wins.
# For example, a pair of eights beats a pair of fives. But if two ranks tie, 
# for example, both players have a pair of queens, 
# then highest cards in each hand are compared.
# If the highest cards tie then the next highest cards are compared and so on.

# The given file contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): 
# the first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid 
# (no invalid characters or repeated cards), 
# each player's hand is in no specific order, 
# and in each hand there is a clear winner.
# How man hands does Player 1 win?
#_____________________________________________________________________________
import os
os.chdir('C:\\Users\\ACER\\Desktop\\FMF\\UVP\\Project_Euler')

def is_straight(numbers):
    numbers.sort()
    if len(numbers) == 5:
        return all(numbers[i + 1] - numbers[i] == 1 for i in range(4))
    else:
        return False

def is_flush(cards):
    return all(cards[i][1] == cards[i + 1][1] for i in range(4))

def value_of_hand(cards, values):
    numbers = [] # this will be a list of numbers without repetitions
    numbers_with_reps = [] 
    for card in cards:
        number = values[card[0]]
        if number not in numbers:
            numbers.append(number)
        numbers_with_reps.append(number)
    repetitions = [numbers_with_reps.count(i) for i in numbers]
    repetitions.sort()
    repetitions.reverse()   # descending order
    numbers_sorted_by_reps = []
    for rep in range(1, max(repetitions) + 1):
        numbers_with_this_rep = [
            i for i in numbers if numbers_with_reps.count(i) == rep
        ]
        numbers_sorted_by_reps += sorted(numbers_with_this_rep)
    numbers_sorted_by_reps.reverse()        # descending order
    #_______________________________________________________________
    if is_flush(cards) and is_straight(numbers):    # straight flush
        return [(2, 1, 1), repetitions, numbers_sorted_by_reps]
    elif repetitions == (4, 1):  # 4 of a kind
        if is_flush(cards):
            return [(2, 1, 0), repetitions, numbers_sorted_by_reps] # 4 of a kind + flush
        else:
            return [(2, 0, 0), repetitions, numbers_sorted_by_reps] # just 4 of a kind
    elif repetitions == (3, 2):      # full house
        if is_flush(cards):
            return [(1, 1, 0), repetitions, numbers_sorted_by_reps]      # full house + flush
        else:
            return [(1, 0, 0), repetitions, numbers_sorted_by_reps]      # just full house
    elif is_flush(cards):
        return [(0, 1, 0), repetitions, numbers_sorted_by_reps]  # flush + something
    elif is_straight(numbers):
        return [(0, 0, 1), repetitions, numbers_sorted_by_reps]  # straight + something
    else:
        return [(0, 0, 0), repetitions, numbers_sorted_by_reps]  # something

def poker(list_of_hands):
    values = {}
    for value, key in enumerate('23456789TJQKA', 2):
        values[key] = value
    #___________________________________________________
    wins_for_player1 = 0
    for hand in list_of_hands:
        player1, player2 = hand[:5], hand[5:]
        if value_of_hand(player1, values) > value_of_hand(player2, values):
            wins_for_player1 += 1
    return wins_for_player1

with open('poker.txt', encoding = 'utf-8') as file:
    rounds = file.read().strip().split('\n')
    
hands = []
for i in rounds:
    hands.append(i.split(' '))

print(poker(hands))