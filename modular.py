from bezoud import bezoud

def invers_modular(k, n):
    # Fem k^-1 (mod n) -> Quan li passem a = 405 i b = 128 a bezoud
    res, a, b, p, q = bezoud(n, k)
    # Sempre el quart paràmetre!!! -> p per obterni l'invers modular.
    if res != 1: 
        return None
    
    return p % n

# print(invers_modular(128, 405))

i = 1
n = 6
while i < n:
    print(str(i) + "^-1 (mod " + str(n) + ") = " + str(invers_modular(i, n)))
    i += 1