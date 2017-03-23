
import random

base62_strings = "Wg2NHiClpf6EYcjxmPQLGOakXhtnD4eFVqd5wRI3rU0J8TKSub19vzMo7AsZyB"
# to make it less boring.. but it needs to be hardcoded, ow it will change
#shuffled = list(base62_strings)
#random.shuffle(shuffled)

size = len(base62_strings) # has to be 62
encoder = dict((symbol, i) for (i, symbol) in enumerate(base62_strings))

#base strings needs to be a set..

def encode(number):
    if number==0: 
        return base62_strings[0]
    code_list=[]
    while number>0:
        code_list.append(base62_strings[number % size])
        number = number / size
    return ''.join(code_list)

def decode(code):
    return sum(encoder[x] * size**i for (i,x) in enumerate(code))