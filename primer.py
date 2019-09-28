import math

def primer(n):
    if n < 2: 
        return False
    
    sqrt = math.sqrt(n)
    for k in range(2, int(sqrt) + 1):
        if n % k == 0:
            return False

    return True
