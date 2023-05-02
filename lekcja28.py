class Test:
 def __del__(self):
      print("bye class")
obj = Test()
obj2 = obj
lista = [obj2]
del obj
del obj2

print("koniec")
