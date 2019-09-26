import random
from utils import generateRandomValue
from utils import getNumber
digits = 1000

def bezoud():
    print("algoritme d'euclides")
    print("--------------------")
    print("Entra si vols que s'autogenerin els numeros o si prefereixes entrar-los tu.")
    print("- 0 -> Generats amb un nombre aleatori de 1 a " + str(digits) + " digits")
    print("- 1 -> A manija")
    option = getNumber("Escull una opcio : ")
    a = 0
    b = 0
    if(option == 0): 
        a = generateRandomValue(random.randint(1, digits))
        b = generateRandomValue(random.randint(1, digits))
    else:    
        a = getNumber("enter the first number: ")
        b = getNumber("enter the second number: ")

    print("Els nombres que s'utilitzen son : ")
    print("")
    print(a)
    print("")
    print(b)
    print("")
    print("Calculem el MCD ...")
    print("")
    # Considerem a com a divident i b com a divisor
    q = 0
    p = 1
    qact = 1
    pact = 0

    while(a % b != 0):
        
        tmp = b
        b = a % b 
        a = tmp