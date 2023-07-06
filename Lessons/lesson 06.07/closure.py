def outer(twice=True, param=0):
    print("outer", param)

    def inner():
        print("inner")
        if twice:
            print("inner")

    return inner


f = outer(False)
print(f, type(f))

# f()
# f()

def degree(n):
    def inner(k):
        return k**n
    return inner

square = degree(2)
cube = degree(3)

for i in range(5):
    print(square(i), cube(i))

# hundred = degree(100)
# hundred() error

print(degree(100)(2))