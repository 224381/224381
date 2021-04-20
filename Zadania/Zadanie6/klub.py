class Klub:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.posiada_trenera = False

    def nadaj_trenera(self):
        self.posiada_trenera = True

    def sprawdz(self):
        if self.posiada_trenera:
            wynik = 'Klub ' + self.nazwa + ' posiada trenera'
        else:
            wynik = 'Klub ' + self.nazwa + ' nie posiada trenera'
            return wynik
