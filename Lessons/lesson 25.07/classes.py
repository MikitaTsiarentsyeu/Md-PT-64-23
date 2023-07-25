class Dog:

    name = ""
    breed = ""
    color = ""

    def bark(self):
        print(f"Woof! My name is {self.name}")

d = Dog()
another_d = Dog()
print(d.name, d.breed, d.color)
d.name = "Zephirka"
d.breed = "wss"
d.color = "white"
print(d.name, d.breed, d.color)
print(another_d.name, another_d.breed, another_d.color)
another_d.name = "Max"
another_d.breed = "german shepherd"
another_d.color = "multi"
print(d.name, d.breed, d.color)
print(another_d.name, another_d.breed, another_d.color)
d.bark()
# another_d.bark()