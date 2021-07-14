# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were 
# written out in words, how many letters would be used? 
# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) 
# contains 20 letters. 
# The use of "and" when writing out numbers 
# is in compliance with British usage.
#________________________________________________________________

def amount_of_letters_for_number(n):
    base = [
        '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
        'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    tens = [
        '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 
        'eighty','ninety'
        ]
    if n == 1000:
        return len('one thousand') - 1  # -1 because spaces don't count
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return len(base[n // 100]) + len('hundred')
        elif n % 100 < 20:
            return (len(base[n // 100]) + len('hundred and') - 1 + 
        + len(base[n % 100]))
        elif n % 100 >= 20:
            return (len(base[n // 100]) + len('hundred and') - 1 + 
            len(tens[(n % 100) // 10]) + len(base[n % 10]))
    elif 20 <= n < 100:
        return len(tens[(n % 100) // 10]) + len(base[n % 10])
    elif 0 <= n < 20:
        return len(base[n])

def number_letter_counts():
    letters_used = 0
    for i in range(1001):
        letters_used += amount_of_letters_for_number(i)
    return letters_used

print(number_letter_counts())