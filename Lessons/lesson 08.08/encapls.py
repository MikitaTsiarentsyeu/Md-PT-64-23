class Engine:

    def __init__(self, power, volume):
        self.__power = power
        self.__volume = volume

    def get_power(self):
        return self.__power
    
    def get_volume(self):
        return self.__volume
    
    power = property(get_power)
    volume = property(get_volume)

class SerialCar:

    __colors = ("black", "white", "grey")

    def __init__(self, make, model, color, engine):
        self.__make = make
        self.__model = model
        self.set_color(color)
        self.engine = engine

    def set_color(self, color):
        if color in SerialCar.__colors:
            self.__color = color
        else:
           self.__color = SerialCar.__colors[0] 

    def get_color(self):
        return self.__color.upper()
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    color = property(get_color, set_color)
    
engine = Engine(100, 2.0)

c = SerialCar("ford", "fiesta", "white", engine)
print(c.get_color())

c.set_color("red")
print(c.get_color())

c.color = "white"
print(c.color)

c.engine = Engine(150, 3.0)

print(c.engine.power)

class SuperCar:

    __colors = ("black", "white", "grey")

    def __init__(self, make, model, color, power, volume):
        self.__make = make
        self.__model = model
        self.set_color(color)
        self.__engine = Engine(power, volume)

    def set_color(self, color):
        if color in SerialCar.__colors:
            self.__color = color
        else:
           self.__color = SerialCar.__colors[0] 

    def get_color(self):
        return self.__color.upper()
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    color = property(get_color, set_color)

    def get_engine_power(self):
        return self.__engine.power
    
    def get_engine_volume(self):
        return self.__engine.volume
    
    power = property(get_engine_power)
    volume = property(get_engine_volume)


SuperCar("ferarri", "la ferarri", "red", 200, 5.0)