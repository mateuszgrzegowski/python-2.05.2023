lista = list(range(10))

print(lista)

nowa = [i * 2 for i in lista]

print("Nowa;", nowa)

nowa2 = [i + 2 for i in lista if i % 2 == 0]

print("Nowa 2:", nowa2)

#Formatowanie stringow

argumenty = ["Mateusz", 29]

tekst = "Cześć mam na imię {imie} i mam {wiek} lata.{imie}".format(imie  = argumenty[0], wiek = argumenty[1])

print(tekst)