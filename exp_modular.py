import utils
import euclides

def esCarmichael(p):
# p > 0
# Retorna cert si p és un nombre de carmichael, fals altrament
    i = 1
    while i < p:
        if euclides.sonCoprimers(i, p):
            if utils.potencia_modular_eficient(i, p-1, p) != 1: 
                return False
        i += 1
    
    if i == p: 
        s = utils.factors_primers(p)
        if len(set(s)) == len(s) and len(s) >= 3: 
            return True

    return False

