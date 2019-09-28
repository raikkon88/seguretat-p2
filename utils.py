import math
import random


def potencia_modular_eficient(base, expo, p):
# p>1
# retorna (baseexpo) mod p
    if expo == 0: # 0 elevat a 0 és 1
        return 1
    elif base==0:
        return 0
    else:
        base_to_exp_div2 = potencia_modular_eficient(base, expo//2, p)
        if expo%2 == 0:
            return (base_to_exp_div2* base_to_exp_div2) % p
        else:
            return (base_to_exp_div2* base_to_exp_div2 * base) % p

def getNumber(text):
# Mostra un text per pantalla
# Recull un nombre per teclat i el retorna
    number = input(text)
    try:
        return int(number)
    except: 
        print ("bad input, retry").unicode('utf-8')
        return getNumber(text)

def generateRandomValue(length):
# Genera un valor aleatori de length xifres
    number = random.randint(1, 9)
    i = 1
    while(i < length):
        number *= 10 
        number += random.randint(1, 10)
        i += 1

    return number

def esPrimer(p):
# p > 0
# Retorna cert si p és primer, falç altrament
    i = 1
    while i < p and potencia_modular_eficient(i, p-1, p) == 1:
        i += 1
        
    if i == p:
        return True
    else: 
        return False


def factors_primers(nombre): 
# nombre > 0
# Retorna el llistat de factors primers del nombre nombre
    llista_fp = []
    if nombre >= 2: 
        d = 2
        while d <= math.sqrt(nombre):
            if nombre % d == 0: 
                llista_fp.append(d)
                nombre = nombre / d
            else: 
                d = d+1

        llista_fp.append(int(nombre))

    return llista_fp

