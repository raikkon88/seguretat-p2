from bezoud import bezoud
import utils

def invers_modular(k, n):
    # Fem k^-1 (mod n) -> Quan li passem a = 405 i b = 128 a bezoud
    res, a, b, p, q = bezoud(n, k)
    # Sempre el quart paràmetre!!! -> p per obterni l'invers modular.
    if res != 1: 
        return None
    return p % n

def log_discret(n, base, arg):
    i = 0
    while arg != utils.potencia_modular_eficient(base, i, n):
        i += 1
    return i

#i = 1
#n = 6
#while i < n:
#    print(str(i) + "^-1 (mod " + str(n) + ") = " + str(invers_modular(i, n)))
#    i += 1

# Exemple = print(log_discret(23,3,12)) Ha de donar 4!