import utils
import euclides

def esCarmichael(p):
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



#p = getNumber("Entra el nombre que vols veure la seva primalitat : ")
#esPrimer(p)
#print(esCharmichael(p))

#for j in range(50000):
#    if esCarmichael(j): 
#        print(j)

# print(esOscarMayer(541))
print(esCarmichael(547))
#print("Finish")


