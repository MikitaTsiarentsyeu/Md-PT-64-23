class Dog:

    name = "Zephirka"
    breed = "wss"
    color = "white"

    def bark(self):
        print("Woof!")

print(Dog.__dict__)

dd = Dog()

d = Dog()
print(d.__dict__)
d.name = "Max"
d.breed = "shepherd"
d.color = "black"
print(d.__dict__)

print(dd.__dict__)

d.bark()

d.bark = "woof"
print(d.__dict__)

# d.bark() error