#filtry i mapy

liczby = [2, 10 ,12, 15, 20, 25, 30 ,35]

#mapy

def funkcja(x):
    return x * 2

wynik = map(funkcja, liczby)

print(list(wynik))

wynik2 = map (lambda x: x + 2 , liczby)

print(list(wynik2))

#filtry

wynik3 = filter (lambda x: x % 2 == 0, liczby )

print(list(wynik3))