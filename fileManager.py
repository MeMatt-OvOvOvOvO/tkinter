import shutil, os, send2trash

class pliczek():
    def __init__(self):
        """Inicjacja atrybutow"""
        self.sciezkaFolderu = ''
        self.sciezkaPliku = ''
        self.nazwaFolderu = ''
        self.nazwaPliku = ''
        self.rozszerzeniePliku = ''

    def utworzFolder(self):
        """funkcja tworzaca folder"""
        print('Folder wlasnie sie tworzy\n')
        nazwaFolderu = str(input('Podaj nazwe folderu: '))
        os.mkdir(nazwaFolderu)

    def utworzPlik(self):
        """Funkcja tworzaca Plik"""
        print('Plik wlasnie sie tworzy\n')
        nazwaPliku = str(input('Podaj nazwe pliku: '))
        rozszerzeniePliku = str(input('Podaj rozszerzenie pliku: '))
        nazwaPliczku = nazwaPliku + '.' + rozszerzeniePliku
        with open(nazwaPliczku, 'w') as fileContent:
            fileContent = ''

    def kopiujFolder(self):
        """Funkcja kopiujaca folder"""
        print('kopiowanie folderu\n')
        sciezkaFolderu = str(input('Podaj nazwe folderu: '))
        nastepnaSciezkaFolderu = str(input('Podaj nazwe nowego folderu: '))
        shutil.copytree(sciezkaFolderu, nastepnaSciezkaFolderu)

    def kopiujPlik(self):
        """Funkcja kopiujaca Plik"""
        print('kopiowanie pliku\n')
        sciezkaPliku = str(input('Podaj nazwe pliku z rozszerzeniem: '))
        nastepnaSciezkaFolderu = str(input('Podaj nazwe z rozszerzeniem nowego pliku: '))
        shutil.copy(sciezkaPliku, nastepnaSciezkaFolderu)

    def zmienNazwePlikuFolderu(self):
        """Funkcja zmieniajaca nazwe pliku lub folderu"""
        print('Zmienianie nazwy pliku lub folderu\n')
        nazwaPliku = str(input('Podaj nazwe pliku lub folderu ktorego nazwa ma byc zmieniona(do pliku dodaj rozszerzenie): '))
        nastepnaNazwaPliku = str(input('Podaj nowa nazwe pliku lub folderu: '))
        os.rename(nazwaPliku, nastepnaNazwaPliku)

    def przeniesPlikFolder(self):
        """Funkcja przenoszaca plik lub folder"""
        print('Przenoszenie pliku lub folderu\n')
        sciezkaPliku = str(input('Podaj sciezke do pliku lub folderu(do pliku dodaj rozszerzenie): '))
        sciezkaDocelowa = str(input('Podaj sciezke dokad chcesz przeniesc plik lub folder: '))
        shutil.move(sciezkaPliku, sciezkaDocelowa)

    def kasacja(self):
        """Funkcja kasujaca plik lub folder"""
        print('Kasowanie pliku lub   folderu\n')
        nazwaPliku = str(input('Podaj nazwe pliku lun folderu ktory chcesz skasowac(do pliku dodaj rozszerzenie): '))
        send2trash.send2trash(nazwaPliku)

plikczek = pliczek()

while(1 == 1):
    print('Menager plikow!!')
    print('Menu: ')
    print('1.Utworz folder')
    print('2.Utworz plik')
    print('3.Kopiuj folder')
    print('4.Kopiuj plik')
    print('5.Zmien nazwe pliku lub folderu')
    print('6.Prenies plik lub folder')
    print('7.Kasuj plik lub folder')
    print('8.Koniec!!')
    twojWybor = int(input('twoj ruch: '))
    if twojWybor == 1:
        plikczek.utworzFolder()
    elif twojWybor == 2:
        plikczek.utworzPlik()
    elif twojWybor == 3:
        plikczek.kopiujFolder()
    elif twojWybor == 4:
        plikczek.kopiujPlik()
    elif twojWybor == 5:
        plikczek.zmienNazwePlikuFolderu()
    elif twojWybor == 6:
        plikczek.przeniesPlikFolder()
    elif twojWybor == 7:
        plikczek.kasacja()
    else:
        break











