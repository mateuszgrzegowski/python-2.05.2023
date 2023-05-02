#klasy i obiekty

class czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    imie = "sebastian"

    def przedstawsie(self, powitanie = 'czesc'):
        return powitanie + ",mam na imie " + self.imie + "lat" + str(self.wiek) + "."

obiekt = czlowiek("sebastian", 24)
print(obiekt.imie)
print(obiekt.przedstawsie("witam"))

obiekt2 = czlowiek("mateusz", 29)
obiekt2.imie = "mateusz"
print(obiekt2.przedstawsie())