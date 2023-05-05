# You are given the following information, 
# but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, 
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during 
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#_______________________________________________________
# 1st January 1901 was a Tuesday

import time

def counting_sundays():
    sundays_on_the_first = 0
    date_of_sunday = 6
    for year in range(1, 101):      # 1 century 
        for month in range(1, 13):
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    while date_of_sunday <= 29:
                        date_of_sunday += 7
                    date_of_sunday %= 29
                else:
                    while date_of_sunday <= 28:
                        date_of_sunday += 7
                    date_of_sunday %= 28
            elif month in {4, 6, 9, 11}:
                while date_of_sunday <= 30:
                    date_of_sunday += 7
                date_of_sunday %= 30
            elif month in {1, 3, 5, 7, 8, 10, 12}:
                if year == 100 and month == 12:
                    break
                while date_of_sunday <= 31:
                    date_of_sunday += 7
                date_of_sunday %= 31
            if date_of_sunday == 1:
                sundays_on_the_first += 1
    return sundays_on_the_first

def main():
    start = time.time()
    resitev = counting_sundays()
    end = time.time()
    cas = round(end - start, 2)
    print(f"resitev = {resitev}\nporabljen cas = {cas}")

main()