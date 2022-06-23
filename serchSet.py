class Podzbiory:
    def x(self, x):
        """funkcja sortujaca"""
        return self.z([], sorted(x))

    def z(self, aktualne, x):
        """funkcja zwracajaca"""
        if x:
            return self.z(aktualne, x[1:]) + self.z(aktualne + [x[0]], x[1:])
        return [aktualne]

q = []
w = int(input('Podaj liczbe elementow w zbiorze: '))

for i in range(0, w):
    element = int(input('Wpisz liczbe: '))
    q.append(element)

print('Podzbiory: ')
print(Podzbiory().x(q))