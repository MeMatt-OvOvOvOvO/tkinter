from math import pi
from koloModule import Kolo

class Kula(Kolo):
    def __init__(self, r):
        """Inicjacja promienia"""
        self.r = r

    def polePowierzchni(self):
        """funkcja liczaca pole powierzchni kuli"""
        return 4 * pi * self.r * self.r

    def objetosc(self):
        """funkcja liczaca objetosc kuli"""
        return (4 * pi * self.r ** 3) / 3