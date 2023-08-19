class FreightTrain:

    def __init__(self, cart_count) -> None:
        self.cart_count = cart_count

    def __str__(self) -> str:
        return f"I'm a train of {self.cart_count} carts, choo-choo!"
    
    def __repr__(self) -> str:
        return f"FreightTrain({self.cart_count})"
    
    def __int__(self):
        return self.cart_count
    
    def __len__(self):
        return int(self)
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.cart_count == other
        
        if not isinstance(other, FreightTrain):
            return False
        
        return self.cart_count == other.cart_count
    
    def __add__(self, other):
        try:
            if isinstance(other, int):
                return FreightTrain(self.cart_count+other)
            return FreightTrain(self.cart_count+other.cart_count)
        except:
            raise TypeError("cannot add non-FreightTrain object")


        

train = FreightTrain(5)
print(repr(train))
print(int(train))
print(len(train))

long = FreightTrain(20)
shorty = FreightTrain(3)
print(long == shorty)
print(long == 20)
# print(20 == long)

print(long+shorty)
print(long+3)
print(3+long)