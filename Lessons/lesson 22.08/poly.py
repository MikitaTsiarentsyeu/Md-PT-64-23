class Animal:

    def SaySomething(self):
        print("Hello, I'm an animal")

class Human:

    def SaySomething(self):
        print("Hello, I'm human")

class Humanomal(Human, Animal):
    pass

class Cat(Animal):

    def SaySomething(self):
        print("Nya")

class Dog(Animal):

    def SaySomething(self):
        print("Woof!")

class Stone:
    pass

def call_SaySomething(obj):
    obj.SaySomething()

a = Animal()
h = Human()
s = Humanomal()
c = Cat()
d = Dog()

for elem in [a, h, s, c, d]:
    call_SaySomething(elem)

