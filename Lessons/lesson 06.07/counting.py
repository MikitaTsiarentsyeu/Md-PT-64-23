# count = 0

counters = {}

# def counter(n):

#     def inner():
#         key = id(inner)
#         counters[key] += 1
#         return counters[key]
    
#     key = id(inner)
#     counters[key] = n
    
#     return inner

def counter(n):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

from_10 = counter(10)
from_100 = counter(100)

print(from_100())
print(from_100())
print(from_10())
print(from_10())

print(counters)

counters[id(from_10)] = 333
print(from_10())
print(from_10())
