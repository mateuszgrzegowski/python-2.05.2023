print(",".join(["a", "b", "c"])) #join łaczenie

print("Witaj Świecie".replace("Witaj", "Cześć")) #replace zastepuje jedno słowo drugim jakie podamy

print("to jest zdanie".startswith("to"))

print("to jest zdanie".endswith("."))

print("j" in "to jest zdanie") # czy j wystepuje w zdaniu ktore podalismy

print("to jest zdanie".upper()) #konwersja zdania na duze litery

print("to jest zdanie".lower()) #konwertuje zdanie na male litery

print("---------------")

lista = [10, 20, 26, 36, 40]

if all([i % 2 == 0 for i in lista]):
    print("Wszystkie parzyste")

if any([i % 2 == 0 for i in lista]):
    print("Chociaż 1 parzysta")


for i in enumerate(lista):
    print(i[0] +1 , "-", i[1])
