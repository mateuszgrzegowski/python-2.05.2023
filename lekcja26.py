class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(animal):
    def voice(self):
        print("how how")

class Cat(animal):
    def getVoice(self):
        print("miau miau")

class Wolf(Dog):
    def getVoice(self):
        print("jestem wilkiem")
        super().voice()

dog = Dog("reksio" ,10)

print(dog.name)

print(dog.age)

dog.voice()

cat = Cat("bury" , 8)
cat.getVoice()

wolf = Wolf("gerald" ,55)
wolf.getVoice()
print(wolf.name)
