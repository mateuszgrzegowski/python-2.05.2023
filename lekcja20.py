def funkcja(f, liczba):
    return f(liczba)

print(funkcja(lambda x: x * x, 3))

def kwadrat(x):
    return x * x

print(kwadrat(5))

wyn = (lambda x: x * x)(5)

print(wyn)

lam = lambda x: x * x
print(lam(5))
print(lam(4))

lam2 = lambda x , y: x * y
print(lam2(2, 3))
print((lambda x,y: x + y)(5, 6))