x = "x"
a = "a"
b = "b"

def print_x(x):
    print(x)

def another_print_x(x):
    print(x)

print_x(a)
another_print_x(b)

x = "test"
for x in range(10):
    x + 1

print(x)

x = "test value for test func"
def test_func():
    print(x)
    test_var = "test"

# print(test_var)

test_func()

def outer_func():
    # x = "outer"
    def inner_func():
        # x = "inner"
        print(x)
        print("it's inner")
    print("it's outer")
    print(x)
    inner_func()

outer_func()

[x+1 for x in range(10)]
print(x)