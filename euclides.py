
def getNumber(text):
    number = input(text)
    try:
        return int(number)
    except: 
        print("bad input, retry")
        return getNumber(text)

def euclides():
    print("algoritme d'euclides : ")
    a = getNumber("enter the first number: ")
    b = getNumber("enter the second number: ")
 
    
    # Considerem a com a divident i b com a divisor
    while(a % b != 0):
        b = a % b 

    print(a * b)


euclides()