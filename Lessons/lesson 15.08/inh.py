class Animal:

    name = "animal"

    def say_something(self):
        print(f"hello, I'm {self.name}")

class Dog(Animal):

    name = "buddy"

    def bark(self):
        print("Woof!")

a = Animal()
print(a.name)
a.say_something()
a.test = "test"
a.name = "new animal"

d = Dog()
print(d.name)
d.say_something()
d.bark()

class Animal:

    def __init__(self, name, spec) -> None:
        self.__spec = spec
        self.__name = name
        
    def get_spec(self):
        return self.__spec
    
    def get_name(self):
        return self.__name
    
    spec = property(get_spec)
    name = property(get_name)

print(Animal.__dict__)
a = Animal("cat", "Simba")
print(a.__dict__)

class Dog(Animal):

    def __init__(self, name, spec=None) -> None:
        super().__init__(name, spec if spec else Dog.__name__)

    def bark(self):
        print("Woof!")

d = Dog("Zefirka")
print(d.name)
d.bark()