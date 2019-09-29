import random
from utils import generateRandomValue
from utils import getNumber

def bezoud(a, b):
# a i b > 0
# retorna per aquest ordre : 
#   mcd(a,b)
#   a que ens han passat com entrada
#   b que ens han passat com entrada
#   Q Pot ser negatiu
#   P Pot ser negatiu
    ina = a
    inb = b
    qant = 0
    pant = 1
    qact = 1
    pact = 0
    iteration = 0

    while(a % b != 0):
        quo = a // b
        qtmp = quo * qact + qant
        ptmp = quo * pact + pant
        qant = qact
        pant = pact 
        qact = qtmp
        pact = ptmp

        tmp = b
        b = a % b 
        a = tmp
        iteration += 1

    if(iteration % 2 == 0): 
        pact *= -1
    else: 
        qact *= -1

    return b, ina, inb, qact, pact

def bezoud_test():
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
        print("The first number must be grather than the second!")
        a = getNumber("enter the first number: ")
        b = getNumber("enter the second number: ")

    ina = a
    inb = b

    print("Els nombres que s'utilitzen son : ")
    print(ina)
    print(inb)
    print("")
    print("Calculem el MCD i la identitat de Bezoud...")
    print("")
    # Considerem a com a divident i b com a divisor
    qant = 0
    pant = 1
    qact = 1
    pact = 0
    iteration = 0

    while(a % b != 0):
        quo = a // b
        qtmp = quo * qact + qant
        ptmp = quo * pact + pant
        qant = qact
        pant = pact 
        qact = qtmp
        pact = ptmp

        tmp = b
        b = a % b 
        a = tmp
        iteration += 1

    if(iteration % 2 == 0): 
        pact *= -1
    else: 
        qact *= -1
    print("MCD : " + str(b))
    print("Q_i : " + str(qact))
    print("P_i : " + str(pact))
    print("Moreover, ... : " + str(b) + " = " + str(qact) + "*" + str(inb) + " + " + str(pact) + "*" + str(ina))

def print_bezoud_result(b, ina, inb, qact, pact):
    print("Moreover, ... : " + str(b) + " = " + str(qact) + "*" + str(inb) + " + " + str(pact) + "*" + str(ina))


#bezoud_test()