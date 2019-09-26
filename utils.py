import random

def getNumber(text):
    number = input(text)
    try:
        return int(number)
    except: 
        print ("bad input, retry").unicode('utf-8')
        return getNumber(text)

def generateRandomValue(length):
    number = random.randint(1, 9)
    i = 1
    while(i < length):
        number *= 10 
        number += random.randint(1, 10)
        i += 1

    return number