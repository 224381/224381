class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie = wynagrodzenie
        self.stala = 2

    def email(self):
        print(self.imie + "." + self.nazwisko + "@testemail.com")

    def pelna_nazwa(self):
        print(self.imie, self.nazwisko)

    def podwyzka(self):
        print(self.wynagrodzenie * self.stala)

dane = Pracownik("Jan", "Kowalski", 2000)
dane.email()
dane.pelna_nazwa()
dane.podwyzka()