import math

def primer(n):
# n > 0
# Retorna cert si n és primer, fals altrament
    if n < 2: 
        return False
    
    sqrt = math.sqrt(n)
    for k in range(2, int(sqrt) + 1):
        if n % k == 0:
            return False

    return True
