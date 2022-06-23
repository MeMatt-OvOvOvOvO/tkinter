import math

class funkcjaKwadratowa():
    def __init__(self, a, b, c):
        """inicjacja atrybutow"""
        self.a = a
        self.b = b
        self.c = c

    def pokaz(self):
        """zapisanie rownania kwadratowego"""
        return f"{self.a}x^2 + {self.b}x + {self.c} = 0"

    def podajX(self):
        """funkcja znajdujaca x"""
        delta = self.b * self.b - 4 * self.a * self.c
        try:
            y = math.sqrt(delta)
        except Exception:
            print('Nie ma rozwiazania')
            return 0
        try:
            x1 = (-self.b + y) / 2
            x1 /= self.a
            x2 = (-self.b - y) / 2
            x2 /= self.a
            if x1 == x2:
                return x1
            return x1, x2
        except Exception:
            print('To nie jest f kwadratowa')

v = funkcjaKwadratowa(0, 12, 4)
print(v.pokaz())
print(v.podajX())