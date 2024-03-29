import time
import matplotlib.pyplot as plt
import numpy as np
from euclides import euclides
from bezoud import bezoud
from utils import generateRandomValue
from utils import getNextPrime
from utils import esPrimer
from primer import primer
from carmichael import esCarmichael
from utils import factors_primers

def euclides_test():

    size = []
    times = []

    i = 1000
    counter = 0
    while i < 50000: 

        # Generem dos nombres aleatoris amb llargada i
        a = generateRandomValue(i)
        b = generateRandomValue(i)

        # Generem una variable on hi desem el codi que executarem per poder calcular el temps. 
        start = time.time()
        euclides(a, b)
        elapsed_time = time.time() - start
        
        size.append(i)
        times.append(elapsed_time)

        i += 2000


    # Generem 25 valors 
    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()


def euclides_examples():
    print(euclides(48, 150))
    print(euclides(150, 48))
    print(euclides(150, 180))
    print(euclides(450, 360))


def bezoud_test():
    size = []
    times = []

    i = 1000
    counter = 0
    while i < 50000: 

        # Generem dos nombres aleatoris amb llargada i
        a = generateRandomValue(i)
        b = generateRandomValue(i)

        # Generem una variable on hi desem el codi que executarem per poder calcular el temps. 
        start = time.time()
        bezoud(a, b)
        
        elapsed_time = time.time() - start
        size.append(i)
        times.append(elapsed_time)

        i += 2000

    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()

def test_primalitat_basic():
    size = []
    times = []
    i = 1
    while i <= 6:
        a = generateRandomValue(i)
        # Obtenim el següent nombre primer de i xifres
        a = getNextPrime(a)
        # Un cop sé que és primer calcule què trigo en verificar-ho
        start = time.time()
        primerR = primer(a)
        elapsed_time = time.time() - start
        if primerR:
            print(i)
            size.append(i)
            times.append(elapsed_time)
        i+=1

    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()

def fermat():
    size = []
    times = []
    i = 1
    while i <= 6:
        a = generateRandomValue(i)
        # Obtenim el següent nombre primer de i xifres
        a = getNextPrime(a)
        print(a)
        # Un cop sé que és primer calcule què trigo en verificar-ho
        start = time.time()
        primerR = esPrimer(a)
        elapsed_time = time.time() - start
        if primerR:
            size.append(i)
            times.append(elapsed_time)
        i+=1

    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()

def test_carmichael():

    size = []
    times = []

    i = 1
    while i < 16000: 
        isCarmichael = esCarmichael(i)
        if isCarmichael: 
            print(i)
            start = time.time()
            esCarmichael(i)
            elapsed_time = time.time() - start

            size.append(i)
            times.append(elapsed_time)
        i += 1

    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()

def test_factors_primers():
    size = []
    times = []

    i = 10
    while i < 100: 
        a = generateRandomValue(i)
        print(a)
        start = time.time()
        factors_primers(a)
        elapsed_time = time.time() - start
        i += 10
        size.append(i)
        times.append(elapsed_time)

    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()


def test_potencia():
    from utils import potencia_modular_eficient

    size = []
    times = []

    # Fixem el valor de l'exponent a un nombre de 100 dígits
    a = generateRandomValue(10)

    i = 1
    while i < 300: 

        # Generem nombre aleatori amb llargada i
        
        base = generateRandomValue(i)
        p = generateRandomValue(i)
        print("Processant operacio -> " + str(base) + "^" + str(a) + "(mod " + str(p) + ")")
        # Generem una variable on hi desem el codi que executarem per poder calcular el temps. 
        start = time.time()
        potencia_modular_eficient(base, a, p)
        elapsed_time = time.time() - start

        size.append(i)
        times.append(elapsed_time)

        i += 1

    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()

def test_log_discret():
    from modular import log_discret

    size = []
    times = []

    # Fixem els valors de la base i del nombre a 3 xifres    
    base = generateRandomValue(3)
    p = generateRandomValue(3)

    i = 1
    while i < 300: 

        # Generem nombre aleatori amb llargada i
        
        base = generateRandomValue(i)
        a = generateRandomValue(i)
        print("Processant operacio -> " + str(base) + "^" + str(a) + "(mod " + str(p) + ")")
        # Generem una variable on hi desem el codi que executarem per poder calcular el temps. 
        start = time.time()
        log_discret(base, a, p)
        elapsed_time = time.time() - start

        size.append(i)
        times.append(elapsed_time)

        i += 1

    plt.plot(size, times, label='linear')
    plt.legend()
    plt.show()

test_log_discret()