#dekoratory

def decorator(func):
    def wrapper():
        print("-------------")
        func()
        print("-------------")
        return wrapper

def hello():
    print("hello world")

hello2 = decorator(hello)
hello2()

print()
@decorator
def witaj():
    print("witaj świecie")

#witaj()

witaj2= witaj
witaj2()
hello()