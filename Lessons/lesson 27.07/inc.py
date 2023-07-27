class Dog:

    __bark_sound = "Woof!"

    def __init__(self, name, breed, color, age=0):
        self.__name = name
        self.__breed = breed
        if breed == "wss":
            self.__color = "white"
        else:
            self.__color = color
        self.__age = age
    
    def bark(self):
        print(self.__bark_sound)

    def get_breed(self):
        return self.__breed
    
    def get_age(self):
        return f"{self.__age} years"
    
    # def set_age(self, new_age):
    #     self.__age = new_age

    def add_year(self):
        self.__age += 1

    def get_color(self):
        return self.__color

d = Dog("Max", "wss", "color")

# print(d.__color)

print(Dog.__dict__)
print(d.__dict__)

print(d.get_breed())

d.bark()

print(d.get_color())