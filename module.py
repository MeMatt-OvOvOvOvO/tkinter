from koloModule import *
from kulaModule import *


while (1 == 1):
    print('Co chcesz policzyc?\n')
    print('1 - Pole kola\n')
    print('2 - Obwod kola\n')
    print('3 - Pole calkowite kuli\n')
    print('4 - Objetosc kuli\n')
    print('Obojetne co - Zakoncz proces\n')
    wybor = int(input())
    if wybor == 1:
        r = float(input('Podaj promien kola: '))
        print('Pole kola to: ' + str(Kolo(r).pole()))
    elif wybor == 2:
        r = float(input('Podaj promien okregu: '))
        print('Obwod okregu to: ' + str(Kolo(r).obwod()))
    elif wybor == 3:
        r = float(input('Podaj promien kuli: '))
        print('Pole calkowite kuli to: ' + str(Kula(r).polePowierzchni()))
    elif wybor == 4:
        r = float(input('Podaj promien kuli: '))
        print('Objetosc kuli to: ' + str(Kula(r).objetosc()))
    else:
        break