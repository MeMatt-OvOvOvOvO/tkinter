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
