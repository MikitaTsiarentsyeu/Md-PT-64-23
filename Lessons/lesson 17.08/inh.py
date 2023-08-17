class FlyingBird:

    def fly(self):
        print("look, mum, I'm flying!")

    def action(self):
        self.fly()


class SwimmingBird:

    def swim(self):
        print("I'm swimming")

    def action(self):
        self.swim()

class Duck(SwimmingBird, FlyingBird): pass

d = Duck()
d.fly()
d.swim()
d.action()

class A:

    def method(self):
        print("A")

class B:

    def method(self):
        print("B")

class C(A, B):

    def method(self):
        print("A")

class D:

    def method(self):
        print("D")

class E:

    def method(self):
        print("E")

class F(E, D):

    def method(self):
        print("F")

class J(F, E, C):

    def method(self):
        print("J")

print(J.__mro__)


class Food:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    def __str__(self):
        return f"{self.type}:{self.name}"

meat = Food("pork", "meat")
print(meat) 

grass = Food("grass", "plant")

class Animal:

    def eat(self, something):
        print(f"eating {something}")

    def phe(self):
        print("phe...")

class Carnivore(Animal):

    def eat(self, something):
        if something.type == "meat":
            Animal.eat(self, something)
        else:
            super().phe()

c = Carnivore()
c.eat(meat)
c.eat(grass)

class Herbivore(Animal):

    def eat(self, something):
        if something.type == "plant":
            Animal.eat(self, something)
        else:
            super().phe()

h = Herbivore()
h.eat(meat)
h.eat(grass)

class Omnivore(Herbivore, Carnivore):

    def eat(self, something):
        if something.type == "plant":
            Herbivore.eat(self, something)
        elif something.type == "meat":
            Carnivore.eat(self, something)
        else:
            super().phe()


print(Omnivore.__mro__)

o = Omnivore()
o.eat(meat)
o.eat(grass)