class Dog: pass

print(Dog, type(Dog))

Dog.test = "test"
# Dog.__dict__["test"] = "test"

print(Dog.__dict__)
print(Dog.test)
print(Dog.__dict__["test"])

d = Dog()
d.test = "new d value"
print(d.__dict__)
print(d.test)
print(d.__dict__["test"])

Dog.new_prop = "value"
print(Dog.new_prop)
print(d.new_prop)