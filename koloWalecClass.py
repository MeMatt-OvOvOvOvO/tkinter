from math import pi
class Kolo():
    def __init__(self, r):
        """inicjacja atrybutow"""
        self.r = r

    def pole(self):
        """funkcja liczaca pole kola o promieniu r"""
        return pi * self.r * self.r

    def obwod(self):
        """funkcja liczaca obwod kola o promieniu r"""
        return 2 * pi * self.r

class Walec(Kolo):
    def __init__(self, h, r):
        """inicjacja atrybutow"""
        super().__init__(r)
        self.h = h

    def poleCalkowite(self):
        """funkcja liczaca pole calkowite walca"""
        return 2 * self.pole() + self.obwod() * self.h

    def objetoscWalca(self):
        """funkcja liczaca objetosc walca"""
        return self.pole() * self.h

while(1 == 1):
    print('Co chcesz policzyc?\n')
    print('1 - Pole kola\n')
    print('2 - Obwod kola\n')
    print('3 - Pole calkowite walca\n')
    print('4 - Objetosc walca\n')
    print('Obojetne co - Zakoncz proces\n')
    wybor = int(input())
    if wybor == 1:
        r = float(input('Podaj promien kola: '))
        print('Pole kola to: ' + str(Kolo(r).pole()))
    elif wybor == 2:
        r = float(input('Podaj promien okregu: '))
        print('Obwod okregu to: ' + str(Kolo(r).obwod()))
    elif wybor == 3:
        r = float(input('Podaj promien podstawy: '))
        h = float(input('Podaj wysokosc walca: '))
        print('Pole calkowite walca to: ' + str(Walec(r, h).poleCalkowite()))
    elif wybor == 4:
        r = float(input('Podaj promien podstawy: '))
        h = float(input('Podaj wysokosc walca: '))
        print('Objetosc walca to: ' + str(Walec(r, h).objetoscWalca()))
    else:
        break