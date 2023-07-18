import time

r = range(100)
print(r, type(r))

def simple_gen():
    print("before fisrt")
    yield 1
    print("before second")
    yield 2
    print("before third")
    yield "test"

gen = simple_gen()
for i in gen:
    print(i)

def even_cubes(l:list):
    for i in l:
        if i % 2 == 0:
            yield i**3

l = [1,2,3,4,5,6,7,8,9,10,11,12]
gen = even_cubes(l)

for i in gen:
    print(i)

print([i**3 for i in l if i % 2 == 0])
print((i**3 for i in l if i % 2 == 0))


def my_range(n):
    counter=0
    while True:
        yield counter
        counter += 1
        if counter == n:
            break

# my_range(10)
# print(list(my_range(10)))
# print(list(my_range(100)))

def fibonacci(n):
    a, b = 0, 1
    counter = 0
    while True:
        yield a
        counter += 1
        if counter == n:
            break
        a, b = b, a+b

start = time.time()
for i in fibonacci(100):
    print(i)
finish = time.time()
print(finish-start)

start = time.time()
list(fibonacci(100))
finish = time.time()
print(finish-start)
